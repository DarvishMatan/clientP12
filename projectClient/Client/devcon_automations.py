""" this file allows me to automate devcon calls """

from subprocess import check_output
import subprocess


"""
get the relevant ids from find * command
msg - send the message got from (devcon find *) into msg
keyWord - send the specific word to be searched
return value is array with all the id's of the specific hardware
"""


def parser(msg, keyWord):
    array = []
    msg = msg.decode()
    lines = str(msg).split("\n")
    for line in lines:
        if line.find(str(keyWord)) != -1:
            good_part = line.split(":")
            good_part = good_part[0].strip()
            array.append(good_part)
    return array


""" returns string with all devices and ids """


def find_all():
    msg = check_output("devcon find *")
    return msg


"""
function to call devcon
command - what to operate
array - the array of ids to be operated (can be NULL)
"""


def callDevcon(command, array):
    for obj in array:
        c = "devcon " + command + " @\"" + obj + "\""
        print(c)
        output = check_output(c)
        print(output.decode())


"""lock the pc"""


def lock():
    devices = find_all()  # find all devices
    mouse_devices = parser(devices, "mouse")  # get mouse
    Mouse_devices = parser(devices, "Mouse")  # get mouse
    keyboard_devices = parser(devices, "Keyboard")  # get keyboard
    #subprocess.call("devcon remove usb*")
    callDevcon("remove", mouse_devices)  # lock mouse
    callDevcon("remove", Mouse_devices)  # lock mouse
    callDevcon("remove", keyboard_devices)  # lock keyboard


""" unlock pc """


def unlock():
    subprocess.call("devcon rescan")


