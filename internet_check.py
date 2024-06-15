# Modules
from speak import say
from requests import get
from attach_audio_file import playAudio
from time import sleep
from assistant_details import aName


def isInternet():
    """
    Check the internet connection.
    :return: True or False.
    """
    url = "http://www.kite.com"
    timeout = 2
    try:
        get(url=url, timeout=timeout)
        return True
    except:
        return False


def isOnline():
    """Check the internet until the internet is connected."""
    counter1 = 1
    counter2 = 0
    if not isInternet():
        while True:
            if isInternet():

                print(f"\rNow the internet is connected back again.")
                playAudio(audioName="Sound\\Internet_connected.wav")
                return say(txt="Now the internet is connected back again.", prnt=False)
            else:
                if counter1 == 1:
                    playAudio(audioName="Sound\\Internet_connection_broken.wav")
                    counter1 = 2
                    print(f"\r{aName}: Internet connection broken.", end="")
                if counter2 == 0 or counter2 == 5 or counter2 % 15 == 0:
                    say(txt="Internet connection broken.", prnt=False)
                counter2 += 1
                sleep(3)
    else:
        return None


if __name__ == '__main__':
    isOnline()
