def find_input_index(input_files: list[dict], name: str) -> int:
    """
    Finds the index of an input file by its name in a list of input files.

    :param input_files: A list of dictionaries representing input files.
                        Each dictionary must have a 'name' key.
    :param name: The name of the input file to find.
    :return: The index of the input file if found, otherwise -1.
    """
    for index, input_file in enumerate(input_files):
        if input_file.get("name") == name:
            return index
    return -1