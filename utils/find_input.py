def find_input(inputs: dict, input_name: str) -> dict:
    """
    Finds and returns a source input by name from the inputs dictionary.

    :param inputs: A dictionary where keys are input names and values are sources.
    :param input_name: The name of the input to find.
    :return: The source corresponding to the input name.
    """
    return inputs.get(input_name)