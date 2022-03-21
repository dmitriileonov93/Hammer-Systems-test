import random
import string


def generate_num_random_string(length):
    rand_string = ''.join(random.sample(string.digits, length))
    return rand_string
