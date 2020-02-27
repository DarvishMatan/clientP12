"""
when client download the software, this is the first commands to be executed
it connects to the website and get the message and the activation
"""


from Client.finals import *
import shelve
import requests
from Client.assisting import *

try:
    createShelfFolder()
except:
    pass


shelf = shelve.open("../vars/vars.txt")  # directory for text file to save the vars
get_activation = "http://defensiveblocks.pythonanywhere.com/clients/" + Finals.USERNAME + "/"
get_message = "http://defensiveblocks.pythonanywhere.com/clientsm/" + Finals.USERNAME + "/"

try:
    r = requests.get(get_activation)
    rm = requests.get(get_message)
except:
    raise Exception("Server Errors")


activation = r.text
message = rm.text
print(activation)
shelf[Finals.messageField] = str(message)
if activation == "0":
    shelf[Finals.activeField] = 0
elif activation == "1":
    shelf[Finals.activeField] = 1
    # TODO START THE LOCK COMMAND

