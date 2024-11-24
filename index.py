import json
from preprocess_clips import preprocess_clips
from parse_inputs import parse_inputs
from parse_tracks import parse_tracks
from parse_output import parse_output


def parse_schema(schema_object_or_string, only_filter_complex: bool = False) -> str:
    """
    Parses a schema and generates an FFmpeg command based on the provided schema.

    :param schema_object_or_string: The schema as a dictionary or JSON string.
    :param only_filter_complex: If True, only returns the filter_complex string.
    :return: The full FFmpeg command or filter_complex string.
    """
    # Parse schema from string or dictionary
    if isinstance(schema_object_or_string, str):
        schema = json.loads(schema_object_or_string)
    else:
        schema = schema_object_or_string

    # Check schema version
    if schema.get("version") != 1:
        raise ValueError("Schema version not supported")

    # Initialize the output command
    output_command = "#!/bin/bash\n"
    input_files = []

    # Preprocess clips
    output_command += preprocess_clips(schema)

    # Start FFmpeg command
    output_command += "ffmpeg -y \\\n"

    # Parse inputs
    inputs_result = parse_inputs(schema)
    output_command += inputs_result["command"]
    input_files.extend(inputs_result["input_files"])

    # Add filter_complex
    output_command += '-filter_complex "'
    filter_complex = parse_tracks(schema, input_files)

    if only_filter_complex:
        return filter_complex

    output_command += filter_complex
    output_command += '" \\\n'

    # Parse output
    output_command += parse_output(schema)

    return output_command