from utils.find_input_index import find_input_index
from utils.uid import get_random_uid


def parse_video_clip(clip: dict, input_files: dict, output: dict) -> str:
    """
    Parses a video or image clip object schema and returns an FFmpeg filter command.

    :param clip: A dictionary representing the video or image clip.
    :param output: A dictionary representing the output configuration.
    :param input_files: A dictionary of input files.
    :return: A string containing the FFmpeg filter command.
    """
    duration = clip["duration"]
    source_start_offset = clip["sourceStartOffset"]
    source = clip["source"]
    transform = clip["transform"]
    name = clip["name"]
    clip_type = clip["clipType"]

    rotation = transform["rotation"]
    opacity = transform["opacity"]
    print(output)
    width = round(transform["width"] * output["scaleRatio"])
    height = round(transform["height"] * output["scaleRatio"])
    x = round(transform["x"] * output["scaleRatio"])
    y = round(transform["y"] * output["scaleRatio"])

    if clip_type == "video":
        input_index = find_input_index(input_files, name)
    else:
        input_index = find_input_index(input_files, source)

    filters = []

    if clip_type == "image":
        # Extend the length of the image video stream
        filters.append(f"loop=loop={duration * output['framerate']}:size={duration * output['framerate']}")

        # Set the start offset of the image video stream
        filters.append("setpts=PTS-STARTPTS")

        # Set the framerate to the output framerate
        filters.append(f"fps={output['framerate']}")

    # Scale the clip to the correct size
    filters.append(f"scale={width}:{height}")

    # Ensure the clip has an alpha channel for opacity adjustments
    filters.append(f"format=rgba,colorchannelmixer=aa={opacity}")

    # Base and clip track layers for rotation and positioning
    base_track_layer_name = f"{get_random_uid(8)}_base"
    clip_track_layer_name = f"{get_random_uid(8)}_clip"

    output_width = round(output["width"] * output["scaleRatio"])
    output_height = round(output["height"] * output["scaleRatio"])

    # Create the base layer with a transparent background
    clip_command = f"color=black@0.0:s={output_width}x{output_height}:d={duration}[{base_track_layer_name}];\n"

    # Add the input and filters
    clip_command += f"[{input_index}:v]{','.join(filters)}[{clip_track_layer_name}];\n"

    post_overlay_filters = []

    # Apply rotation to the combined stream after overlaying
    post_overlay_filters.append(f"rotate={rotation}")

    # Overlay the clip onto the base layer with position and post-overlay filters
    clip_command += f"[{base_track_layer_name}][{clip_track_layer_name}]overlay={x}:{y}:format=auto,{','.join(post_overlay_filters)},fps={output['framerate']}[{name}];"

    return clip_command