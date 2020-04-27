from playsound import playsound
import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def playSong():
    d = os.path.dirname(os.getcwd())
    audio = str(d)
    audio += r"\audio.mp3"
    playsound(audio)


def volumeMax():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Control volume
    volume.SetMasterVolumeLevel(-0.0, None)

def main():
    volumeMax()
    playSong()
    

main()
