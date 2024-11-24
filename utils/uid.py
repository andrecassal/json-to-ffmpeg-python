import random
import string


def get_random_uid(length: int = 8) -> str:
    """
    Generates a random UID of the specified length.

    :param length: The length of the UID to generate (default is 8).
    :return: A randomly generated UID as a string.
    """
    charset = string.ascii_letters + string.digits
    return ''.join(random.choice(charset) for _ in range(length))