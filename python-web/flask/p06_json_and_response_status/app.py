from typing import Tuple, Dict

from flask import (
    Flask, Response
)


app = Flask(__name__)


@app.route('/')
def index() -> Tuple[
    Dict[str, str],
    int,
    Dict[str, str],
]:
    return (
        {
            'name': "Gandalf",
            'occupation': "Wizard"
        },
        203,
        {
            "Content-Type": "application/json"
        },
    )
