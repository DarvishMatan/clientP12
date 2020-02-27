import requests
import shelve
from Client.finals import Finals as final

getActivation = "http://defensiveblocks.pythonanywhere.com/clients/" + final.USERNAME + "/"
# url = "http://127.0.0.1:8000/clients/" + final.USERNAME + "/"
shelf = shelve.open("../vars/vars.txt")


def main():
    global activation
    while True:
        r = requests.get(getActivation)
        activation = r.text
        print(activation)
        if activation == "0":
            activation = 0
            if final.activeField is activation:
                return
            else:
                shelf[final.activeField] = activation
                # TODO CALL THE UNLOCK FUNCTION
                return
        elif activation == "1":
            if final.activeField is activation:
                return
            else:
                shelf[final.activeField] = activation
                # TODO CALL THE LOCK FUNCTION
                return


if __name__ == "__main__":
    main()

