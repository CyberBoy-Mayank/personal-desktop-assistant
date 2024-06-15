# Modules
from internet_check import isOnline
from speech_recognition import Recognizer, Microphone
import assistant_details
import user_details


def listen():
    """Recognize the voice and convert it into text."""
    isOnline()
    r = Recognizer()
    with Microphone() as source:
        print(f"\r{assistant_details.aName}: Listening.....", end="")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source=source, duration=1)
        audio = r.listen(source=source, phrase_time_limit=6)
    try:
        print(f"\r{assistant_details.aName}: Processing.....", end="")
        query = r.recognize_google(audio_data=audio, language='en-IN')
        query = str(query)
        query = query.replace("backup", "wakeup")
        query = query.strip()
        print(f"\n{user_details.uName}: {query}")
    except:
        print(f"\r{assistant_details.aName}: I couldn't Recognize, Please say that again.")
        return 'none'
    return query


if __name__ == '__main__':
    while True:
        listen()
