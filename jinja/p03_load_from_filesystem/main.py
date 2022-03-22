
import jinja2 as j2


def main() -> None:
    print("START")

    e1 = j2.Environment(loader=j2.FileSystemLoader("./dragons"))
    t1 = e1.get_template("kek.html")
    result = t1.render()
    print("RESULT", result)

    print("STOP")


if __name__ == "__main__":
    main()
