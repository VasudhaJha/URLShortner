import os
import random, string

default_length = 8
code_length = os.environ.get('CODE_LENGTH', default_length)

def generate_random_code(length: int=code_length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
