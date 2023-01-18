/*
Enums - definition with initializers
*/


fn main() {

    #[derive(Debug)]
    enum SomeKind {
        Foo,
        Bar {_a: u16},
        Kek(u16),
        Pop(i32, i32),
    }

    let mut x = SomeKind::Foo;
    println!("{:?}", x);

    x = SomeKind::Bar {_a: 777};
    println!("{:?}", x);

    x = SomeKind::Kek(123);
    println!("{:?}", x);

    x = SomeKind::Pop(333, 444);
    println!("{:?}", x);
}
