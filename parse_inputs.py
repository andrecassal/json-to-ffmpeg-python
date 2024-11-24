def parse_inputs(schema: dict) -> dict:
    """
    Parses the inputs from the schema and generates the FFmpeg input command and input files list.

    :param schema: A dictionary representing the VideoEditorFormat schema.
    :return: A dictionary containing the FFmpeg command string and input files.
    """
    inputs_command = ""
    input_files = []

    # Process tracks and their clips
    for track_name, track in schema["tracks"].items():
        for clip in track["clips"]:
            source = clip["source"]
            clip_type = clip["clipType"]
            name = clip["name"]
            temp_dir = schema["output"]["tempDir"]

            if clip_type == "video":
                inputs_command += f"-i {temp_dir}/{name}.mp4 \\\n"
                input_files.append({
                    "file": f"{name}_tmp.mp4",
                    "name": name,
                })

    # Process schema inputs
    for input_name, input_item in schema["inputs"].items():
        if input_item["type"] == "video":
            continue

        inputs_command += f"-i {input_item['file']} \\\n"
        input_files.append({
            "name": input_name,
            "file": input_item["file"],
        })

    return {
        "command": inputs_command,
        "input_files": input_files,
    }