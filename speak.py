# Modules
from pyttsx3 import init
import assistant_details


def say(txt: str, prnt: bool = True, speech: bool = True):
    """
    This function is used to convert text to speech.
    :param txt: str.
    :param prnt: boolean.
    :param speech: boolean.
    :return: engine.runAndWait.
    """
    engine = init(driverName="sapi5")
    voices = engine.getProperty(name='voices')  # To get voices
    engine.setProperty(name='voice', value=voices[assistant_details.aVoice].id)  # To set voices
    engine.getProperty(name='rate')  # To get speech rate
    engine.setProperty(name='rate', value=185)  # To set speech rate
    engine.getProperty(name='volume')  # To get volume
    engine.setProperty(name='volume', value=1)  # To set volume
    if not prnt and speech:  # For only speech.
        engine.say(text=txt)
        return engine.runAndWait()
    elif not speech and prnt:  # For only print.
        return print(f"{assistant_details.aName}: {txt}")
    else:  # For both, speech and print.
        print(f"{assistant_details.aName}: {txt}")
        engine.say(text=txt)
        return engine.runAndWait()
