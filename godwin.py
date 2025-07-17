import sys, os, time
from colorama import init  # type: ignore

init()

NAME = "GODWIN KIPLIMO"
GOLD = "\033[38;2;212;175;55m"
BLINK = "\033[5m"
RESET = "\033[0m"

try:
    while True:
        sys.stdout.write(f"{BLINK}{GOLD}{NAME}{RESET}\r")
        sys.stdout.flush()
        time.sleep(0.5)

        sys.stdout.write(" " * len(NAME) + "\r")
        sys.stdout.flush()
        time.sleep(0.5)

except KeyboardInterrupt:
    os.system("cls" if os.name == "nt" else "clear")
    print("Stopped") 

