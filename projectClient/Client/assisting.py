import os


def createShelfFolder():
    # define the name of the directory to be created
    path = "../vars/"

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
        try:
            path += "vars.txt"
            f = open(path, "a")
            f.close()
        except OSError:
            print("Creation of the directory %s failed" % path)


