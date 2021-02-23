# import sys
# import subprocess
import time
# import webbrowser
import json
# import getpass
# import os
import requests
from io import StringIO

filename = "/home/neo/Documents/Python/Chat/msg.txt"


def delline(del_line, filename):
    with open(filename, "r") as textobj:
        liste = list(textobj)  # puts all lines in a list

    del liste[del_line - 1]  # delete regarding element

    #rewrite the textfile from liste contents/elements:
    with open(filename, "w") as textobj:
        for n in liste:
            textobj.write(n)


while True:
    # if True:
    with open(filename, 'r') as msgfile:
        msglst = msgfile.read().split("\n")
        # for item in msglst:
        for line in range(len(msglst)):
            # print(line)
            try:
                item = msglst[line]
            except:
                continue
            if item == "":
                continue
            io = StringIO(item)
            try:
                msglst = json.load(io)
            except json.decoder.JSONDecodeError:
                delline(line, filename)
                continue
            url = "http://" + str(msglst['notifyhost']) + ":18522/"
            data = {'user': str(msglst['user']),
                    'host': str(msglst['sendhost']), 'msg': str(msglst['msg'])}
            try:
                resp = requests.post(url, data=data)
                print("Send")
                delline(line, filename)
            except requests.exceptions.ConnectionError:
                pass
    time.sleep(5)
