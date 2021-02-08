import string, random

def base62_encoding(length):
    result = ""
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = "0123456789"
    encoding_set =  numbers + lower_case + upper_case #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

    for i in range(length):
        random_idx = random.randint(0,61)
        random_char = encoding_set[random_idx]
        result+= random_char

    return result

    
