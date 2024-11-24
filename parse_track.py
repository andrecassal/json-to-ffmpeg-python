from parse_clip import parse_clip
from utils.uid import get_random_uid


SAFE_FRAMES_FOR_TRANSITION = 2  # Frames to subtract for transition safety

def get_gap_filler(track_type, output, duration):
    """
    Generates a filler for gaps (transparent video or silence).
    """
    gap_label_name = f"gap_{get_random_uid()}"
    width = round(output["width"] * output["scaleRatio"])
    height = round(output["height"] * output["scaleRatio"])

    command = (
        f"color=c=black@0.0:s={width}x{height}:d={duration}[{gap_label_name}];\n"
        if track_type == "video"
        else f"anullsrc=channel_layout=stereo:sample_rate=44100:d={duration}[{gap_label_name}];\n"
    )

    return {"command": command, "gapLabelName": gap_label_name}


def get_xfade_transition(from_label, to_label, duration, transition_type, output, offset, label_prefix="", custom_label=None):
    """
    Generates an xfade transition between two clips.
    """
    framerate = output["framerate"]
    from_intermediate_label = f"fps_{from_label}_{get_random_uid(8)}"
    to_intermediate_label = f"fps_{to_label}_{get_random_uid(8)}"

    transition_label_name = custom_label or f"{label_prefix}_xfade_{get_random_uid()}"

    command = (
        f"[{from_label}]fps={framerate}[{from_intermediate_label}];\n"
        f"[{to_label}]fps={framerate}[{to_intermediate_label}];\n"
        f"[{from_intermediate_label}][{to_intermediate_label}]xfade=transition={transition_type}:duration={duration}:offset={offset},fps={framerate}[{transition_label_name}];\n"
    )

    return {"command": command, "transitionLabelName": transition_label_name}


def get_concat_transition(from_label, to_label, output, label_prefix="", custom_label=None):
    """
    Concatenates two clips.
    """
    framerate = output["framerate"]
    transition_label_name = custom_label or f"{label_prefix}_concat_{get_random_uid()}"
    command = f"[{from_label}][{to_label}]concat=n=2:v=1:a=0,fps={framerate}[{transition_label_name}];\n"
    return {"command": command, "transitionLabelName": transition_label_name}


def parse_track(track_name, track, output, total_length, transitions, input_files):
    """
    Parses a single track into FFmpeg commands.
    """
    clips_command = ""
    clips_to_concat = []
    previous_clip_end_time = 0

    # Process all clips in the track
    for clip in track["clips"]:
        if clip["timelineTrackStart"] > previous_clip_end_time:
            # Fill gaps between clips
            gap_duration = clip["timelineTrackStart"] - previous_clip_end_time
            gap = get_gap_filler(track["type"], output, gap_duration)
            clips_command += gap["command"]
            clips_to_concat.append({
                "label": gap["gapLabelName"],
                "duration": gap_duration,
                "isGap": True
            })

        # Parse individual clip
        clips_command += parse_clip(clip, output, input_files)
        clips_to_concat.append({
            "label": clip["name"],
            "duration": clip["duration"],
            "isGap": False
        })
        previous_clip_end_time = clip["timelineTrackStart"] + clip["duration"]

    # Handle the gap after the last clip
    if previous_clip_end_time < total_length:
        gap_duration = total_length - previous_clip_end_time
        gap = get_gap_filler(track["type"], output, gap_duration)
        clips_command += gap["command"]
        clips_to_concat.append({
            "label": gap["gapLabelName"],
            "duration": gap_duration,
            "isGap": True
        })

    # Process video or audio-specific commands
    if track["type"] == "video":
        clip_group_labels = []
        for current_clip in clips_to_concat:
            original_label = current_clip["label"]

            # Handle transitions from/to void (black screen)
            if current_clip["isGap"]:
                clip_group_labels.append({
                    "label": current_clip["label"],
                    "duration": current_clip["duration"],
                    "isGap": True,
                    "originalLabel": original_label
                })
                continue

            transition_start = next((t for t in transitions if t["from"] is None and t["to"] == original_label), None)
            if transition_start:
                safe_transition_duration = transition_start["duration"] - (1 / output["framerate"]) * SAFE_FRAMES_FOR_TRANSITION
                clips_command += f"color=c=black@0.0:s={round(output['width'] * output['scaleRatio'])}x{round(output['height'] * output['scaleRatio'])}:d={transition_start['duration']}[void_{current_clip['label']}];\n"

                transition_data = get_xfade_transition(
                    from_label=f"void_{current_clip['label']}",
                    to_label=current_clip["label"],
                    duration=safe_transition_duration,
                    transition_type=transition_start["type"],
                    output=output,
                    offset=0,
                    label_prefix="start"
                )
                clips_command += transition_data["command"]
                current_clip["label"] = transition_data["transitionLabelName"]

            clip_group_labels.append({
                "label": current_clip["label"],
                "duration": current_clip["duration"],
                "isGap": False,
                "originalLabel": original_label
            })

        # Combine clips
        previous_clip_group = clip_group_labels[0]
        for i in range(1, len(clip_group_labels)):
            current_clip_group = clip_group_labels[i]
            transition = next((t for t in transitions if t["from"] == previous_clip_group["originalLabel"] and t["to"] == current_clip_group["originalLabel"]), None)
            use_concat = previous_clip_group["isGap"] or current_clip_group["isGap"] or not transition

            transition_data = (
                get_concat_transition(
                    from_label=previous_clip_group["label"],
                    to_label=current_clip_group["label"],
                    output=output,
                    label_prefix="between",
                    custom_label=track_name if i == len(clip_group_labels) - 1 else None
                )
                if use_concat else
                get_xfade_transition(
                    from_label=previous_clip_group["label"],
                    to_label=current_clip_group["label"],
                    duration=transition["duration"] if transition else 0,
                    transition_type=transition["type"] if transition else "fade",
                    output=output,
                    offset=previous_clip_group["duration"] - transition["duration"] if transition else 0,
                    label_prefix="between",
                    custom_label=track_name if i == len(clip_group_labels) - 1 else None
                )
            )

            clips_command += transition_data["command"]
            previous_clip_group = {
                "label": transition_data["transitionLabelName"],
                "duration": previous_clip_group["duration"] + current_clip_group["duration"] - (transition["duration"] if transition else 0),
                "isGap": False,
                "originalLabel": current_clip_group["originalLabel"]
            }

    elif track["type"] == "audio":
        # Concatenate audio clips
        for clip in clips_to_concat:
            clips_command += f"[{clip['label']}]"
        clips_command += f"concat=n={len(clips_to_concat)}:v=0:a=1[{track_name}];\n"

    return clips_command