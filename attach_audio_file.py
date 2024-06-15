# Modules
from playsound import playsound


def playAudio(audioName: str):
    """
    Attach audio file and play it.
    :param audioName: audio file name
    """
    return playsound(audioName)


if __name__ == '__main__':
    playAudio("Sound\\Internet_connection_broken.wav")
    # playAudio("Sound\\Terminate_sound.wav")
