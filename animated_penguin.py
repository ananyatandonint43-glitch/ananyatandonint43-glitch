import os
import sys
import time

# ANSI colors
CYAN = "\033[96m"
BLUE = "\033[94m"
WHITE = "\033[97m"
YELLOW = "\033[93m"
BLACK = "\033[30m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

frames = [
    r"""
       .--.
      |o_o |
      |:_/ |
     //   \ \
    (|     | )
   /'\_   _/`\
   \___)=(___/
    """,
    r"""
       .--.
      |o_o |
      |:_/ |
     //   \ \
    (|     | )
   /'\_   _/`\
   \___)=(___/
     ~ flap ~
    """,
]

def colorize(penguin):
    lines = penguin.splitlines()
    result = []

    for line in lines:
        colored = line
        colored = colored.replace("o_o", f"{YELLOW}o_o{BLACK}")
        colored = colored.replace(":", f"{WHITE}:{BLACK}")
        colored = colored.replace("/", f"{BLUE}/{BLACK}")
        colored = colored.replace("\\", f"{BLUE}\\{BLACK}")
        colored = colored.replace("(", f"{CYAN}({BLACK}")
        colored = colored.replace(")", f"{CYAN}){BLACK}")
        result.append(colored)

    return "\n".join(result)

try:
    while True:
        for frame in frames:
            os.system("cls" if os.name == "nt" else "clear")
            print(CLEAR + colorize(frame) + RESET)
            print(f"\n{CYAN}Penguin party!{RESET}")
            time.sleep(0.5)

except KeyboardInterrupt:
    print(f"\n{WHITE}Penguin waddled away. Bye!{RESET}")
    sys.exit()
