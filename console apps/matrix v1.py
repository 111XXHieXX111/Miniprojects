import string
import random
import time
import sys
import shutil
import os
import traceback

# User settings:

USE_COLORS = True
LINE_INTERVAL = 0.1



chars = string.ascii_letters + "0123456789"

console_width = 0

def init_console():
    global console_width
    
    console_width, console_height = shutil.get_terminal_size()
    print(f"Console size:{console_width}x{console_height}")
    
    if USE_COLORS:
        print("\033[32m")

def get_random_char():
    random_index = random.randint(0, len(chars) - 1)
    return chars[random_index]

def print_line():
    _chars = ""
    
    for _ in range(console_width):
        choice = random.randint(0, 2)
        if choice == 0:
            _chars += get_random_char()
        else:
            _chars += " "
        
    print(_chars)

if __name__ == "__main__":
    if USE_COLORS and os.name == "nt":
        os.system("")
        
    print("Press Ctrl+C for exit!")
    time.sleep(1) 
    init_console()
    
    try:
        while True:
            print_line()
            time.sleep(LINE_INTERVAL)
    except KeyboardInterrupt:
        if USE_COLORS:
            print("\033[0m")
        
        print("Quiting from the script")
        sys.exit()
    except Exception:
        if USE_COLORS:
            print("\033[0m")
        
        traceback.print_exc()
        
        time.sleep(1)
        sys.exit(-1)

# NOTE:
# MATRIX V1
# BY XXHIEXX
# https://github.com/111XXHieXX111/Miniprojects
