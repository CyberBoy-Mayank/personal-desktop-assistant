# Modules
from assistant_details import aName
import speak
from random import choice
from listen import listen
import user_details
from database import updateValue


def textRemover(txt: str):
    """
    This function is used to remove the extra text.
    :param txt: str.
    :return: uName: str.
    """
    txt = txt.replace(aName, "")
    txt = txt.replace("give me the", "")
    txt = txt.replace("my name is", "")
    txt = txt.replace("i want to", "")
    txt = txt.replace("with the", "")
    txt = txt.replace("call me", "")
    txt = txt.replace("my name", "")
    txt = txt.replace("with a", "")
    txt = txt.replace("with", "")
    txt = txt.replace("i am", "")
    txt = txt.replace("name", "")
    txt = txt.replace("call", "")
    txt = txt.replace("you", "")
    txt = txt.replace("can", "")
    txt = txt.replace("i'm", "")
    txt = txt.replace("me", "")
    txt = txt.strip()
    txt = txt.capitalize()
    return txt


def changeUserName():
    """
    This function is used to change the username.
    :return: Change username.
    """

    counter1 = 0
    reply1 = f"What can I call you?", "What's your name?", "What name should I call you?"
    speak.say(f"Okay Sir! {choice(reply1)}")
    while True:
        uNewName = listen().lower()
        uNewName = str(uNewName)
        if counter1 == 4 or counter1 == 9:
            speak.say(f"{choice(reply1)}")
            counter1 += 1
        elif counter1 == 13:
            return speak.say("The command has been canceled because you didn't respond.")
        elif uNewName == 'none':
            counter1 += 1
        elif "exit" in uNewName or "cancel my command" in uNewName or "cancel command" in uNewName or "cancel the command" in uNewName:
            return speak.say(f"Okay sir.")
        elif "you can call me" in uNewName or "my name is" in uNewName or "i am" in uNewName or "i'm" in uNewName or "my name" in uNewName \
                or "call me" in uNewName or "can you call me" in uNewName or "you give me the name" in uNewName or "you give me name" in uNewName \
                or "you can call me with a" in uNewName or "you can call me with" or "can you call me with a" in uNewName \
                or "can you call me with" in uNewName or "my name":
            textRemover(txt=uNewName)
            if uNewName == user_details.uName:
                return speak.say(f"{uNewName} is your current name.")
            else:
                updateValue("memory_status", "user_name", uNewName)
                user_details.userName = str(uNewName)
                return speak.say(f"Of course sir! Now I can call you {uNewName} sir.")
        else:
            counter1 += 1


def dyChangeUName(uNewName: str):
    """
    This function is used to change the username dynamically.
    :param uNewName: str.
    :return: Change username.
    """
    textRemover(txt=uNewName)
    if uNewName == user_details.uName:
        return speak.say(txt=f"{uNewName} is your current name.")
    else:
        updateValue("memory_status", "user_name", uNewName)
        user_details.userName = str(uNewName)
        return speak.say(f"Of course sir! Now I can call you {uNewName} sir.")
