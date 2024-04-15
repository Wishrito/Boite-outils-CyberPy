import os
import webbrowser

import flask
from flask import Request, render_template, request

toolboxApp = flask.Flask(__name__)
toolboxApp.static_folder = os.path.join(os.path.dirname(__file__), 'src')
toolboxApp.template_folder = os.path.join(os.path.dirname(__file__), 'pages')


@toolboxApp.errorhandler(404)
def notFound(request: Request):
    return render_template("404.html"), 404


@toolboxApp.route("/")
def hello():
    """
    This function is used to show the home.html page.

    :return: the rendered home.html page
    """
    return render_template('home.html')


@toolboxApp.route("/bruteforce")
def bruteforce():
    """
    This function is used to show the bruteforce.html page.

    :return: the rendered bruteforce.html page
    """
    return render_template('bruteforce.html')

# partie système, pas besoind d'y toucher
if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 4569
    url = f"http://{HOST}:{PORT}"
    print(url)
    webbrowser.open(url, new=1)
    toolboxApp.run(host=HOST, port=PORT, debug=True)
