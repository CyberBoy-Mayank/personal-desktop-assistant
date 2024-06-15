# Modules
from os import stat
from speak import say
from calendar_time import todayDate, currentTime
from assistant_details import aName


def setReminder(memory: str):
    """Set reminder in Remember.txt file."""
    memory = memory.replace(aName, "")
    memory = memory.replace("this", "")
    memory = memory.strip()
    say(txt=f"You told me to {memory}.")
    memory = memory.replace("remember that", "")
    memory = memory.replace("remember this", "")
    memory = memory.replace("remember", "")
    memory = memory.strip()
    with open("Remember.txt", "w") as Remember:
        Remember.write(f"{todayDate()} {currentTime()} o'clock :-> You told me to remember that {memory}.\n")


def remember():
    """Retrieve the records from the Remember.txt file."""
    file_path = "Remember.txt"
    if stat(file_path).st_size == 0:
        return say(txt="Sir you didn't tell me to remember anything.")
    else:
        with open("Remember.txt", "r") as Remember:
            say(txt=Remember.read())
        with open("Remember.txt", "w"):
            return None
