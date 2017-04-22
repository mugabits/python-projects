# server.py

from flask import Flask, make_response


def main():
    app = Flask(__name__)
    configure(app)

    return app


def configure(app):

    @app.route("/")
    def home():
        return make_response("This is home", 200)


if __name__ == "__main__":
    server = main()
    server.run()
