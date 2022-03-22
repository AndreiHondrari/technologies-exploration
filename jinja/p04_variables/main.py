from wsgiref import headers as wsgi_headers, simple_server
from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from _typeshed.wsgi import WSGIEnvironment, StartResponse

import markdown
import jinja2 as j2


MARKDOWN_1 = """
# Something

## Chapter 1

```python
def f1() -> None:
    for i in range(10):
        print(i)
```

## Chapte 2

"""


def do_jinja() -> str:
    e1 = j2.Environment(loader=j2.FileSystemLoader("./dragons"))

    e1.filters['markdown'] = markdown.markdown

    t1 = e1.get_template("kek.html")
    result = t1.render({
        'part1': '1 2 3 4 5 6',
        'part2': 'Ullamco ut reprehenderit esse enim veniam oris sunt emer.',
        'pieces': [11, 22, 33, 44, 55, 'yahboy'],
        'some_md': MARKDOWN_1,
    })
    return result


def application(
    environ: "WSGIEnvironment",
    start_response: "StartResponse"
) -> Iterable[bytes]:
    headers = wsgi_headers.Headers()
    headers.add_header('Content-Type', 'text/html')
    start_response('200 OK', headers.items())

    content = do_jinja()

    return [content.encode()]


def main() -> None:
    print("START")

    with simple_server.make_server("localhost", 8080, application) as httpd:
        httpd.serve_forever()

    print("STOP")


if __name__ == "__main__":
    main()
