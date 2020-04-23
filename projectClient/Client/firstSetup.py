"""
when client download the software, this is the first commands to be executed
it connects to the website and get the message and the activation
"""
import shelves
from Client.assisting import *




try:
    create_vars_folder()  # create vars folder
    create_var(final.active_field, 0)  # create variable with value 0
    createDesktopFolder()  # create file in desktop
    popup()  # alert for reading the instructions

except:
    pass

