import traceback
import sys
import time
import random

# User settings:

MAX_NUM = 100



print("Write 'quit' for quit or Ctrl+C")

guessed_num = random.randint(0, MAX_NUM)

def check_num(num:str):
    if num.upper() == "QUIT":
        sys.exit(0)
    
    num = int(num)
    
    if num == guessed_num:
        print("You gessed number!")
        time.sleep(1)
        sys.exit(0)
    elif num > guessed_num:
        print("Less")
    elif num < guessed_num:
        print("More")

if __name__ == "__main__":
    try:
        while True:
            num = input()
            check_num(num)
    except Exception:
        traceback.print_exc()
        
        time.sleep(1)
        sys.exit(-1)

    except KeyboardInterrupt:
        print("Quiting from the script")
        sys.exit(0)
