"""A module containing helper functions"""

import string
import random

def base62_encoding(length):
    """ Returns a random string to serve as Slug  """
    result = ""
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = "0123456789"
    encoding_set =  numbers + lower_case + upper_case

    for _ in range(length):
        random_idx = random.randint(0,61)
        random_char = encoding_set[random_idx]
        result+= random_char

    return result
    