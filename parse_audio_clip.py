from utils.find_input_index import find_input_index


def parse_audio_clip(clip: dict, input_files: dict) -> str:
    """
    Parses an audio clip object schema and returns an FFmpeg filter command.

    :param clip: A dictionary representing the audio clip.
    :param input_files: A dictionary of input files.
    :return: A string containing the FFmpeg filter command for the audio clip.
    """
    # Extract properties from the clip
    duration = clip["duration"]
    source_start_offset = clip["sourceStartOffset"]
    source = clip["source"]
    volume = clip["volume"]
    name = clip["name"]

    # Find the input index
    input_index = find_input_index(input_files, source)

    # Create filters
    filters = []

    # Use the atrim filter to set the start offset and duration
    filters.append(f"atrim={source_start_offset}:{source_start_offset + duration}")

    # Reset the presentation timestamp to 0 after trimming
    filters.append("asetpts=PTS-STARTPTS")

    # Set the volume of the audio clip
    filters.append(f"volume={volume}")

    # Construct the FFmpeg filter command
    return f"[{input_index}:a]{','.join(filters)}[{name}];"