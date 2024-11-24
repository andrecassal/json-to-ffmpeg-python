from calculate_total_length import calculate_total_length
from parse_track import parse_track
from utils.uid import get_random_uid


def parse_tracks(schema: dict, input_files: dict) -> str:
    """
    Loop over each track, parse it, and combine as two streams: one for video and one for audio.

    :param schema: The schema dictionary representing the video editor format.
    :param input_files: A dictionary of input files.
    :return: A string containing the FFmpeg commands to process tracks.
    """
    # Calculate the total length of the video
    total_length = calculate_total_length(schema["tracks"], schema.get("transitions", []))

    # Create a black base video stream
    width = round(schema["output"]["width"] * schema["output"]["scaleRatio"])
    height = round(schema["output"]["height"] * schema["output"]["scaleRatio"])
    tracks_command = f"color=c=black:s={width}x{height}:d={total_length}[base];\n"

    # Parse each track
    for track_name, track in schema["tracks"].items():
        tracks_command += parse_track(
            track_name=track_name,
            track=track,
            output=schema["output"],
            total_length=total_length,
            transitions=schema.get("transitions", []),
            input_files=input_files,
        )

    # Combine video tracks into a single video stream
    video_tracks = [
        track_name for track_name, track in schema["tracks"].items() if track["type"] == "video"
    ]
    audio_tracks = [
        track_name for track_name, track in schema["tracks"].items() if track["type"] == "audio"
    ]

    previous_track_name = "base"
    for i, video_track_name in enumerate(video_tracks):
        combined_overlay_name = (
            "video_output"
            if i == len(video_tracks) - 1
            else f"{get_random_uid(8)}_combined_track"
        )

        tracks_command += f"[{previous_track_name}][{video_track_name}]overlay=0:0[{combined_overlay_name}];\n"
        previous_track_name = combined_overlay_name

    # Combine audio tracks by mixing them together
    for audio_track_name in audio_tracks:
        tracks_command += f"[{audio_track_name}]"

    if len(audio_tracks) > 1:
        tracks_command += f"amix=inputs={len(audio_tracks)}:duration=longest[audio_output];"
    elif len(audio_tracks) == 1:
        tracks_command += f"volume=1[audio_output];"
    else:
        tracks_command += f"anullsrc=channel_layout=stereo:sample_rate=44100:d={total_length}[audio_output];"

    return tracks_command