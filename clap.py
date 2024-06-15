import sounddevice as sd
import numpy as np
from wish_me import wishMe

threshold = 90
Clap = False


def detect_clap(indata, frames, time, status):
    global Clap
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > threshold:
        print("Fuck You")
        Clap = True


def Llisten_for_claps():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)


if __name__ == '__main__':
    while True:
        Llisten_for_claps()
        if Clap:
            wishMe()
            break
        else:
            pass
