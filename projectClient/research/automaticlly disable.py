from subprocess import check_output


"""
send the message got from (devcon find *) into msg
send the specific word to be searched
return value is array with all the id's of the specific hardware
"""
def parser(msg, keyWord):
    array = []
    lines = msg.split("\n")
    for line in lines:
        if line.find(str(keyWord)) != -1:
            good_part = line.split(":")
            good_part = good_part[0].strip()
            array.append(good_part)
    return array


def find_all():
    msg = check_output("devcon find *")
    return msg


"""
function to call devcon
command - what to operate
array - the array of ids to be operated (can be NULL)
"""


def callDevcon(command, array):
    for obj in array:
        output = check_output("devcon " + str(command) + " " + obj)


"""usage example:"""


def main():
    out = find_all()
    important = parser(out,"Mouse")  # find the 'Mouse' (case-sensetive) id
    callDevcon("disable",important)
