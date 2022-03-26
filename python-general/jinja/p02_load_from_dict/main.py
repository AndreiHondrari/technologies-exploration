
import jinja2 as j2

TEMPLATE_MAPPING = {
    'potato': "Hello my dark friend!",
}


def main() -> None:
    print("START")

    e1 = j2.Environment(loader=j2.DictLoader(TEMPLATE_MAPPING))
    t1 = e1.get_template("potato")
    result = t1.render()
    print("RESULT", result)

    print("STOP")


if __name__ == "__main__":
    main()
