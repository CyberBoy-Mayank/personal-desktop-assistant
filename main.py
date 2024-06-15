# Modules
from internet_check import isInternet
from subprocess import run, PIPE
from assistant_details import aName
from wish_me import wishMe


def start():
    counter = 0
    while True:
        if not isInternet():
            run(["python", "internet_check.py"], stdout=PIPE, stderr=PIPE)
            print(f"\r{aName}: Please Connect The Internet.", end="")
        else:
            print()
            if counter == 0:
                wishMe()
                counter = 1
            from start import main
            main()


if __name__ == '__main__':
    start()
