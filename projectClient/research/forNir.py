import requests
import time
import sys

"""
        url = "http://127.0.0.1:8000/clientsm/" + USERNAME + "/"
        r = requests.get(url)
        print(r.text)
        """
def main():
    while True:
        USERNAME = "matandarvish"
        url = "http://127.0.0.1:8000/clients/" + USERNAME + "/"
        r = requests.get(url)
        activation = r.text
        if activation == "0":
            return
        elif activation == "1":
            return

        time.sleep(60)


if __name__ == "__main__":
    main()
