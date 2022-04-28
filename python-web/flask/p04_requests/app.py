from string import Template

from flask import Flask, url_for, request, Request


app = Flask(__name__)

INDEX_HTML_TEMPLATE = Template("""
<h1>Index</h1>

<form action="$index_url" method="POST">
    <input type="text" name="gandalf"/>
</form>
""")


RESULT_HTML_TEMPLATE = Template("""
<h1>RESULT</h1>
<a href="$index_url">Back to index</a>
<p>You typed: $text</p>
""")


def show_index() -> str:
    return INDEX_HTML_TEMPLATE.substitute(
        index_url=url_for("index")
    )


def process_index_req(request: Request) -> str:

    return RESULT_HTML_TEMPLATE.substitute(
        index_url=url_for("index"),
        text=request.form.get('gandalf', 'N/A')
    )


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    if request.method == "GET":
        return show_index()

    elif request.method == "POST":
        return process_index_req(request)
