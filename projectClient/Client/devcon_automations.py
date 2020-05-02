from subprocess import check_output
import subprocess


"""
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



def lock():
    devices = find_all()
    mouse_devices = parser(devices, "mouse")
    Mouse_devices = parser(devices, "Mouse")
    Keyboard_devices = parser(devices, "Keyboard")
    keyboard_devices = parser(devices, "keyboard")
    #subprocess.call("devcon remove usb*")
    callDevcon("remove", mouse_devices)
    callDevcon("remove", Mouse_devices)
    callDevcon("remove", keyboard_devices)
    callDevcon("remove", Keyboard_devices)


def unlock():
    subprocess.call("devcon rescan")


