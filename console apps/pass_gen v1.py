import traceback
import sys
import string
import random
import time

# User settings

PASSWORD_LEN = 32
PASSWORDS_COUNT = 16



chars = string.ascii_letters + "0123456789"

def get_random_char():
    random_index = random.randint(0, len(chars) - 1)
    return chars[random_index]

def generate_password():
    output = ""
    
    for _ in range(PASSWORD_LEN):
        output += get_random_char()
    
    return output

if __name__ == "__main__":
    try:
        for _ in range(PASSWORDS_COUNT):
            password = generate_password()
            print(password)
    except Exception:
        traceback.print_exc()
        time.sleep(1)
        sys.exit(-1)

# NOTE:
# PASS GEN V1
# BY XXHIEXX
# https://github.com/111XXHieXX111/Miniprojects
