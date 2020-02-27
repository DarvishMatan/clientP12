import subprocess
from time import sleep

def Lock_Access():
    subprocess.Popen("devcon disable usb*")
   
def Open_Access():
    subprocess.Popen("devcon rescan")
    subprocess.Popen("devcon /r enable usb*")
   
Lock_Access()
sleep(6)
Open_Access()