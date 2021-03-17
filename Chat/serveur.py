# import time
import getpass
import os
import subprocess
import sys

localhostname = os.uname()[1]
localuser = getpass.getuser()
# while True:
if True:
    distantuser = sys.argv[1]
    distanthost = sys.argv[2]
    message = sys.argv[3]
    args = [
        "ssh",
        "-l",
        distantuser,
        distanthost,
        "notify-send",
        localuser + "@" + localhostname,
        message,
    ]
    subprocess.Popen(args=args)
    # time.sleep(5)
