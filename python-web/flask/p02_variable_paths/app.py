from flask import Flask


app = Flask(__name__)


@app.route('/')
def index() -> str:
    return """
    <h1>Home</h1>
    <a href="/some/111">Potato 1</a><br/>
    <a href="/some/222">Potato 2</a>
    """


@app.route('/some/<int:potato>')
def some(potato: int) -> str:
    return f"<p>My potato: {potato}</p>"
