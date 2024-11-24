def parse_output(schema: dict) -> str:
    """
    Parses the output schema object and returns the FFmpeg command
    with flags and arguments configured in options.

    :param schema: The schema dictionary containing output configuration.
    :return: A string containing the FFmpeg command for the output.
    """
    output_command = ""

    # Extract output parameters from the schema
    output = schema["output"]
    file = output["file"]
    framerate = output["framerate"]
    video_codec = output["videoCodec"]
    audio_codec = output["audioCodec"]
    width = output["width"]
    height = output["height"]
    flags = output.get("flags", [])
    audio_bitrate = output["audioBitrate"]
    crf = output["crf"]
    preset = output["preset"]
    start_position = output["startPosition"]
    end_position = output["endPosition"]
    scale_ratio = output["scaleRatio"]

    # Process additional flags
    additional_flags = " ".join(flags) if flags else ""

    # Calculate resolution based on scale ratio
    render_width = round(width * scale_ratio)
    render_height = round(height * scale_ratio)
    resolution = f"{render_width}x{render_height}"

    # Construct the output FFmpeg command
    duration = end_position - start_position
    output_command += (
        f"-map '[video_output]' -map '[audio_output]' "
        f"-c:v {video_codec} -c:a {audio_codec} "
        f"-b:a {audio_bitrate} -r {framerate} -s {resolution} "
        f"-ss {start_position} -t {duration} "
        f"-crf {crf} -preset {preset} {additional_flags} {file}"
    )

    return output_command