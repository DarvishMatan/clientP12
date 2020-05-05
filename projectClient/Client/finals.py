"""
each client has finals like username

TODO get the username when download the software


"""
import os


class Finals:
    UN = os.environ['USERNAME']
    USERNAME = os.environ['COMPUTERNAME']
    msg_field = "message"
    active_field = 'activation'
    thread = "thread_field"
    path = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\vars\vars.txt" % UN
    first_setup_path = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\vars" % UN
    first_setup_path = first_setup_path + "\\"
    print(first_setup_path)
