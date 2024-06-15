# Modules
from listen import listen
from process import process
import assistant_details
from os import startfile

hotWord = assistant_details.aName.lower()


def main():
    startfile("battery_status.py")
    query = listen().lower()
    if hotWord in query:
        query = query.replace(hotWord, "")
        query = query.strip()
        if query != '' or query != "none":
            return process(query=query)
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    while True:
        main()
