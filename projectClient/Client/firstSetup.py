"""
when client download the software, this is the first commands to be executed
it connects to the website and get the message and the activation
"""
import shelves
from Client.assisting import *




try:
    create_vars_folder()
    create_var(final.active_flag, 0)
    create_var(final.active_field, 0)
    create_var(final.messageField, "")
except:
    pass


"""
activation = r.text
message = rm.text
print(activation)
shelf[Finals.messageField] = str(message)
if activation == "0":
    shelf[Finals.activeField] = 0
elif activation == "1":
    shelf[Finals.activeField] = 1
    # TODO START THE LOCK COMMAND

"""
