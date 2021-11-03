import attr


if __name__ == '__main__':

    SomeClass = attr.make_class("SomeClass", ['a', 'b'])
    o1 = SomeClass(a="foo", b=123)
    print("o1", o1)

    SomeClassB = attr.make_class("SomeClassB", {
        'a': attr.ib(type=int),
        'b': attr.ib(type=str),
    })
    o1 = SomeClassB(a="foo", b=123)
    print("o1", o1)
