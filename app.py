from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "<h1>Hello!</h1><p>Text</p>"


if __name__ == "__main__":
    app.run()
