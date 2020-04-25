import os
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
from Client2.finals import Finals as final
import ctypes

def popup():
    ctypes.windll.user32.MessageBoxW(0, "Instruction text file named DefensiveBlocks.txt has created. Please read it.", "DefensiveBlocks", 1)


def createDesktopFolder():
    username = os.getlogin()    # Fetch username
    file = open(f'C:\\Users\\{username}\\Desktop\\DefensiveBlocks.txt','w')
    file.write('Please signup in our site in order to use our service.\n link: https://defensiveblocks.pythonanywhere.com/\n with username = ' + str(os.environ['COMPUTERNAME']))
    file.close()


def exb():
    pass


"""
I had to replace shelve - in order to save vars forever (shelve doesnt work)
this are the funcs

"""


def create_vars_folder():
    # define the name of the directory to be created
    path = "../vars/"

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


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



