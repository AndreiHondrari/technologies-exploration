from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def index() -> str:
    return (
        f"<h1>Home</h1>"
        f"<a href=\"{url_for('this')}\">This</a><br/>"
        f"<a href=\"{url_for('that')}\">That</a>"
    )


@app.route('/some/<int:potato>')
def some(potato: int) -> str:
    return f"<p>My potato: {potato}</p>"


@app.route("/this")
def this() -> str:
    return "<h1>THIS</h1>"


@app.route("/that")
def that() -> str:
    return "<h1>THAT</h1>"
