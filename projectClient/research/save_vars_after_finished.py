import fileinput
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove


path = "../vars/vars.txt"


""" this func is for first setup - to create the vars"""
def create_var(var,value):
    append_con = open(path, "a")
    append_con.write(str(var) + ',' + str(value) + "\n")
    append_con.close()


def replace(pattern, value):
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(path) as old_file:
            for line in old_file:
                parts = line.split(",")
                if str(parts[0]) == str(pattern):
                    new_file.write(line.replace(line, pattern + "," + str(value) + "\n"))
                else:
                    new_file.write(line)
    copymode(path, abs_path)
    remove(path)
    move(abs_path, path)


def get(pattern):
    read_con = open(path, "r")
    content = read_con.read()
    lines = content.split("\n")
    for line in lines:
        parts = line.split(",")
        if str(parts[0]) == str(pattern):
            return parts[1].strip("\n")


create_var("ophir",2)
create_var("o",4)
create_var("p",0)
replace("o",100)
print(get("o"))


