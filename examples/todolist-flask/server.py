# server.py

from flask import Flask


def main():
    app = Flask(__name__)
    configure(app)

    return app


def configure(app):

    @app.route("/")
    def home():
        return "This is home"


if __name__ == "__main__":
    server = main()
    server.run()
