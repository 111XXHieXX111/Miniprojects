import traceback
import sys
import string
import secrets
import time

# User settings

PASSWORD_LEN = 32
PASSWORDS_COUNT = 16
USE_PUNCT_CHARS = True



chars = string.ascii_letters + string.digits

if USE_PUNCT_CHARS:
    chars += string.punctuation

def generate_password():
    output = ""
    
    for _ in range(PASSWORD_LEN):
        output += secrets.choice(chars)
    
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
# PASS GEN V2
# BY XXHIEXX
# https://github.com/111XXHieXX111/Miniprojects
