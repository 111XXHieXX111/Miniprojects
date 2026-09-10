import traceback
import string
import sys
import time

print("Write 'quit' for quit or Ctrl+C")

def get_solution(example:str):
    out_example = ""
    
    if example.upper() == "QUIT":
        print("Quiting from the script")
        sys.exit(0)
    
    for char in example:
        if char not in string.ascii_letters:
            out_example += char

    if out_example == "":
        return

    return str(eval(out_example))

if __name__ == "__main__":
    try:
        while True:
            example = input()
            solution = get_solution(example)
            print(solution)
    except Exception:
        traceback.print_exc()
                
        time.sleep(1)
        sys.exit(-1)

    except KeyboardInterrupt:
        print("Quiting from the script")
        sys.exit(0)
        