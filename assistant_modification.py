# Modules
import assistant_details
import speak
from listen import listen
from database import updateValue


def txtRemover(txt: str):
    """This function is used to remove extra text from the given query."""
    txt = txt.replace(assistant_details.aName, "")
    txt = txt.replace("i give you the name", "")
    txt = txt.replace("i give you name", "")
    txt = txt.replace("call you with a", "")
    txt = txt.replace("i give you the", "")
    txt = txt.replace("i give you", "")
    txt = txt.replace("i want to", "")
    txt = txt.replace("with the", "")
    txt = txt.replace("call you", "")
    txt = txt.replace("your is", "")
    txt = txt.replace("with a", "")
    txt = txt.replace("can i", "")
    txt = txt.replace("i can", "")
    txt = txt.replace("name", "")
    txt = txt.replace("your", "")
    txt = txt.replace("with", "")
    txt = txt.strip()
    txt = txt.capitalize()
    return txt


def changeAssistantName():
    """Change assistant name."""
    counter = 0
    speak.say(txt="Okay sir! What do you want to call me?")
    while True:
        aNewName = listen().lower()

        if aNewName == "exit" in aNewName or "cancel the command" in aNewName or "cancel my command" in aNewName or "cancel command" in aNewName or \
                "i dont want to give you any new name" in aNewName or "i don't want to give you any new name" in aNewName or \
                "i dont want to give you new name" in aNewName or "i don't want to give you new name" in aNewName:
            return speak.say(txt="Okay sir!")
        elif counter == 4 or counter == 9:
            speak.say(txt="Please tell me sir! What do you want to call me?")
            counter += 1
        elif counter == 13:
            return speak.say(txt="The command has been canceled because you didn't respond.")
        elif aNewName == 'none':
            counter += 1
        elif "i want to call you" in aNewName or "can i call you" in aNewName or "i give you the name" in aNewName or \
                "i give you name" in aNewName or "i can call you" or "can i call you with a" in aNewName or \
                "can i call you" in aNewName or "your name is" in aNewName or "your name" in aNewName or "can i call you with the":
            aNewName = txtRemover(txt=aNewName)
            if aNewName == assistant_details.aName:
                speak.say(txt=f"{aNewName} is my current name.")
                speak.say(txt="Please give me a unique name.")
                counter = 0
            else:
                updateValue("memory_status", "assistant_name", aNewName)
                assistant_details.aName = str(aNewName)
                print(f"{assistant_details.aName}: Now you can call me {assistant_details.aName}.")
                return speak.say(txt=f"Now you can call me {aNewName}.", prnt=False, speech=True)
        else:
            counter = 1


def dyChangeAName(aNewAName: str):
    """Change assistant name dynamically."""
    aNewAName = txtRemover(txt=aNewAName)
    if aNewAName == assistant_details.aName:
        speak.say(txt=f"{aNewAName} is my current name.")
        return speak.say(txt=f"Please give me a unique name.")
    else:
        updateValue("memory_status", "assistant_name", aNewAName)
        assistant_details.aName = aNewAName
        print(f"{assistant_details.aName}: Now you can call me {assistant_details.aName}.")
        return speak.say(txt=f"Now you can call me {assistant_details.aName}.", prnt=False, speech=True)


def changeAVoice():
    """Change assistant voice."""
    counter = 0
    if assistant_details.aVoice == 1:
        updateValue("memory_status", "assistant_voice", "0")
        assistant_details.aVoice = 0
        speak.say(txt="Here's an example of one of my other voices, Would you like me to use this one?")
        while True:
            query = listen().lower()
            if counter == 4 or counter == 9:
                speak.say(txt="Here's an example of one of my other voices, Would you like me to use this one?")
                counter += 1
            elif counter == 13:
                updateValue("memory_status", "assistant_voice", "1")
                assistant_details.aVoice = 1
                return speak.say(txt="The command has been canceled because you didn't respond.")
            elif query == 'none' or query == "":
                counter += 1
            elif "cancel my command" in query or "cancel the command" in query or "cancel the my command" in query:
                return speak.say(txt="Okay sir!")
            elif "i like it" or "yes" in query or "ok" in query or "okay" in query:
                return speak.say(txt="My voice has changed.")
            elif "no" in query:
                updateValue("memory_status", "assistant_voice", "1")
                assistant_details.aVoice = 1
                return speak.say(txt="Okay sir.")
            else:
                speak.say(txt="Do you want me to use this voice?")
    elif assistant_details.aVoice == 0:
        updateValue("memory_status", "assistant_voice", "1")
        assistant_details.aVoice = 1
        speak.say(txt="Here's an example of one of my other voices, Would you like me to use this one?")
        while True:
            query = listen().lower()
            if counter == 4 or counter == 9:
                speak.say(txt="Here's an example of one of my other voices, Would you like me to use this one?")
                counter += 1
            elif counter == 13:
                updateValue("memory_status", "assistant_voice", "0")
                assistant_details.aVoice = 0
                return speak.say(txt="The command has been canceled because yu didn't respond.")
            elif query == "none" or query == "":
                counter += 1
            elif "cancel my command" in query or "cancel the command" in query or "cancel the my command" in query:
                return speak.say(txt="Okay sir!")
            elif "i like it" or "yes" in query or "ok" in query or "okay" in query:
                return speak.say(txt="My voice has changed.")
            elif "no" in query:
                updateValue("memory_status", "assistant_voice", "0")
                assistant_details.aVoice = 0
                return speak.say(txt="Okay sir.")
            else:
                speak.say(txt="Do you want me to use this voice?")


if __name__ == '__main__':
    changeAVoice()
