import pickle
import os


def create_vars_folder():
    # define the name of the directory to be created
    path = "../vars/"

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
        try:
            path += "vars.txt" # save vars.txt as final
            f = open(path, "a")
            f.close()
        except OSError:
            print("Creation of the directory %s failed" % path)
create_vars_folder()

with open("../vars/vars.txt", "wb") as f:
    pickle.dump("first", f)
    pickle.dump("second", f)

with open("../vars/vars.txt", 'rb') as f:
    first = pickle.load(f)
    second = pickle.load(f)
    s = pickle.load(f)



