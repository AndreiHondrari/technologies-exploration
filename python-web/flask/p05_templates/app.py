from string import Template

from flask import (
    Flask, url_for,
    request, render_template,
)


app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template('index.html')
