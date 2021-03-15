"""Server to save sended messages"""
import json
import os
from flask import Flask, Response, request
os.environ["FLASK_ENV"] = "deployment"

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """## Index page."""
    if request.method == 'POST':
        user = request.form['user']
        notifyhost = request.form['notifyhost']
        msg = request.form['msg']
        sendhost = request.form['sendhost']
    else:
        user = request.args.get('user')
        notifyhost = request.args.get('notifyhost')
        sendhost = request.args.get('sendhost')
        msg = request.args.get('msg')

    print(request.remote_addr)
    # if socket.gethostbyname(sendhost) == request.remote_addr:
    #     print("Vrai")
    # else:
    #     print("SPAM")
    #     print(socket.gethostbyname(sendhost))
    #     print(request.remote_addr)
    #     return "SPAM"
    jsonvalue = json.dumps(
        {'user': user, 'notifyhost': notifyhost, 'sendhost': sendhost, 'msg': msg})
    resp = Response(jsonvalue)
    resp.headers['Content-type'] = 'application/json'
    with open("/home/neo/Documents/Python/Chat/msg.txt", "a") as file:
        file.write(jsonvalue+"\n")
    with open("/home/neo/Documents/Python/Chat/msg_svgd.txt", "a") as file:
        file.write(jsonvalue+"\n")
    return resp


port = 18523
if __name__ == "__main__":
    # webbrowser.open("http://localhost:"+str(port))
    app.run(debug=False, port=port, host='0.0.0.0')
    # app.run(port=port)
