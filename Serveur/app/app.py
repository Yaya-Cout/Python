u"""# Flask server app"""
import os

import wikipedia as wikipediaapp
from flask import Flask, render_template, request, send_from_directory

# import webbrowser

os.environ["FLASK_ENV"] = "deployment"

app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    u"""Adding favicon."""
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="static/favicon.ico",
    )


@app.route("/")
def index():
    """## Index page."""
    # return "<h1>Bienvenue sur le site</h1>"
    return render_template("/index.html")


@app.route("/wikipedia")
@app.route("/wikipedia/")
def wikipediaindex():
    u"""## index of wikipedia folder."""
    return render_template("/wikipedia/index.html")


@app.route("/wikipedia/page.html", methods=["GET", "POST"])
def wikipediapage():
    u"""## View wikipedia page."""
    if request.method == "POST":
        page = request.form["page"]
    else:
        page = request.args.get("page")
    page_py = wikipediaapp.wiki_wiki.page(page)
    # page = page_py.summary
    return render_template("/wikipedia/page.html", page=page, page_py=page_py)


port = 8080
if __name__ == "__main__":
    # webbrowser.open("http://localhost:"+str(port))
    app.run(debug=True, port=port)
    # app.run(port=port)
