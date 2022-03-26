
import jinja2 as j2


def give_some(name: str) -> str:
    print("GET_TEMPLATE", name)
    return "Hello my dark friend!"


def main() -> None:
    print("START")

    e1 = j2.Environment(loader=j2.FunctionLoader(give_some))
    t1 = e1.get_template("kek")
    result = t1.render()
    print("RESULT", result)

    print("STOP")


if __name__ == "__main__":
    main()
