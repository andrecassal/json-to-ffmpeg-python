from parse_video_clip import parse_video_clip
from parse_audio_clip import parse_audio_clip

def parse_clip(clip: dict, output: dict, input_files: dict) -> str:
    """
    Routes the parsing of different clip types (video, image, audio) to their respective parsers.

    :param clip: A dictionary representing the clip to be parsed.
    :param output: A dictionary representing the output configuration.
    :param input_files: A dictionary of input files.
    :return: A string containing the parsed clip information.
    """
    clip_string = ""

    if clip["clipType"] in ["video", "image"]:
        clip_string += parse_video_clip(clip, input_files, output)
    elif clip["clipType"] == "audio":
        clip_string += parse_audio_clip(clip, input_files)

    return clip_string + "\n"