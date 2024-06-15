# Modules
from assistant_details import aName
from pyautogui import press
from math import ceil
from speak import say


def textRemover(query):
    """
    Extra text remover.
    :param query: str.
    :return: query: str.
    """
    query = str(query)
    query = query.replace(aName, "")
    query = query.replace("percentage", "")
    query = query.replace("increase", "")
    query = query.replace("decrease", "")
    query = query.replace("can you", "")
    query = query.replace("volume", "")
    query = query.replace("percen", "")
    query = query.replace("person", "")
    query = query.replace("three", "3")
    query = query.replace("seven", "7")
    query = query.replace("eight", "8")
    query = query.replace("voice", "")
    query = query.replace("point", "")
    query = query.replace("four", "4")
    query = query.replace("five", "5")
    query = query.replace("nine", "9")
    query = query.replace("ten", "10")
    query = query.replace("down", "")
    query = query.replace("one", "1")
    query = query.replace("two", "2")
    query = query.replace("six", "6")
    query = query.replace("the", "")
    query = query.replace("up", "")
    query = query.replace("of", "")
    query = query.replace("%", "")
    query = query.strip()
    try:
        query = int(query)
        return query
    except:
        pass


def volumeUp(query: str):
    """
    This function is used to increase the volume.
    :param query: str.
    :return: Volume up.
    """
    try:
        if query == "can you increase volume" or query == "can you increase the volume" or query == "volume up" \
                or query == "volume increase" or query == "increase the volume" or query == "increase volume" \
                or query == "increase the volume up" or query == "increase volume up":
            for _ in range(5):
                press('volumeup')
        else:
            query = textRemover(query=query)
            query = query / 2
            ceilValue = ceil(query)
            for _ in range(ceilValue):
                press('volumeup')
    except:
        return say(txt="Something wants wrong.")


def volumeDown(query: str):
    """
    This function is used to Decrease the volume.
    :param query: str.
    :return: volume down.
    """
    try:
        if query == "can you decrease volume" or query == "can you decrease the volume" or query == "volume down" \
                or query == "volume decrease" or query == "decrease the volume" or query == "decrease volume" \
                or query == "decrease the volume down" or query == "decrease volume down":
            for _ in range(5):
                press('volumedown')
        else:
            query = textRemover(query=query)
            query = query / 2
            ceilValue = ceil(query)
            for _ in range(ceilValue):
                press('volumedown')
    except:
        return say(txt="Something wants wrong.")


def volumeMax():
    """
    This function is used to Maximize the volume.
    :return: full volume.
    """
    for _ in range(50):
        press('volumeup')


def volumeMute():
    """
    This function is used to mute volume.
    :return: volume mute.
    """
    return press('volumemute')
