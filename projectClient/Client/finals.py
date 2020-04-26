"""
each client has finals like username

TODO get the username when download the software


"""
import os


class Finals:
    UN = os.environ['USERNAME']
    USERNAME = os.environ['COMPUTERNAME']
    active_field = 'activation'
    thread = "thread_field"
    path = "../vars/vars.txt"
    first_setup_path = "../vars/"

print(Finals.UN)
