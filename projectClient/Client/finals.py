"""
this is finals vars file
"""

import os


class Finals:
    UN = os.environ['USERNAME']  # username - use it for startup
    USERNAME = os.environ['COMPUTERNAME']  # username for the user
    active_field = 'activation'  # field in the vars file
    path = "../vars/vars.txt"  # path for vars file
    first_setup_path = "../vars/"  # path for vars folder
    repeats = "0,15,30,45"  # send requests every 15 seconds
