"""Server to save sended messages"""
import json
import os
from os.path import expanduser

import notify2
from flask import Flask, Response, request

home = expanduser("~")
os.environ["FLASK_ENV"] = "deployment"

app = Flask(__name__)
notify2.init("Chat")


@app.route("/", methods=["GET", "POST"])
def index():
    """## Index page."""
    if request.method == "POST":
        print("post")
        user = request.form["user"]
        host = request.form["host"]
        msg = request.form["msg"]
    else:
        print("get")
        user = request.args.get("user")
        host = request.args.get("host")
        msg = request.args.get("msg")

    with open(home + "/.local/share/blablachathist.txt", "a") as hist:
        hist.write(json.dumps({"user": user, "host": host, "msg": msg}) + "\n")
    n = notify2.Notification(
        user + "@" + host,
        msg,
        #  "notification-message-im"   # Icon name
    )
    n.set_timeout(notify2.EXPIRES_NEVER)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.show()
    # return "<h1>Bienvenue sur le site</h1>"+user+"<br>"+host+"<br>"+msg+"<br>"
    resp = Response(json.dumps({"user": user, "host": host, "msg": msg}))
    resp.headers["Content-type"] = "application/json"
    return resp


port = 18522
if __name__ == "__main__":
    # webbrowser.open("http://localhost:"+str(port))
    app.run(debug=False, port=port, host="::")
    # app.run(port=port)
