import os
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
from finals import Finals as final
import ctypes

""" display popup, show the user that instruction file has created """


def popup():
    ctypes.windll.user32.MessageBoxW(0, "Instruction text file named DefensiveBlocks.txt has created. Please read it.", "DefensiveBlocks", 1)


""" create desktop file with the instructions """


def createDesktopFolder():
    username = os.getlogin()    # Fetch username
    file = open(f'C:\\Users\\{username}\\Desktop\\DefensiveBlocks.txt','w')  # open the file in the wanted place 
    file.write('Please signup in our site in order to use our service.\n link: https://defensiveblocks.pythonanywhere.com/\n with username = ' + str(os.environ['COMPUTERNAME']))
    file.close()


""" when close/minimize button clicked, ignore (tkinter)"""


def exb():
    pass


"""
I had to replace shelve - in order to save vars forever (shelve doesnt work)
this are the funcs.
vars are located in vars.txt file. 
the structor is - "var_name,value"

"""


""" create vars folder in order to locate the vars.txt file """


def create_vars_folder():
    # define the name of the directory to be created
    path = "../vars/"

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


""" this function creates a variable, the vars model is: name_of_var,value. var is the name, value is the value """


def create_var(var,value):
    append_con = open(final.path, "a")  # append type - add text
    append_con.write(str(var) + ',' + str(value) + "\n")  # structure
    append_con.close()


""" this function changes the value of a var. pattern is the var name, value is the value u want """


def replace(pattern, value):
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:  # create new file, change the vars values
        with open(final.path) as old_file:
            for line in old_file:
                parts = line.split(",")  # the structure
                if str(parts[0]) == str(pattern):
                    new_file.write(line.replace(line, pattern + "," + str(value) + "\n"))
                else:
                    new_file.write(line)
    copymode(final.path, abs_path)
    remove(final.path)
    move(abs_path, final.path)


""" this function returns the value of a var. patten = var name """    


def get(pattern):
    read_con = open(final.path, "r+")  # read the values
    content = read_con.read()
    lines = content.split("\n")  # split by pattern
    for line in lines:
        parts = line.split(",")  # split by pattern
        if str(parts[0]) == str(pattern):
            return parts[1].strip("\n")
    read_con.close()

