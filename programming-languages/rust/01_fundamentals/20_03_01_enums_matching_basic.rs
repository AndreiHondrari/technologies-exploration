/*
Enums - pattern matching
*/


fn main() {

    #[derive(Debug)]
    enum SomeKind {Foo, Bar, Kek}

    let x = SomeKind::Kek;
    println!("defined -> {:?}", x);

    let y = match x {
        SomeKind::Foo => 11,
        SomeKind::Bar => 22,
        SomeKind::Kek => 33,
    };

    println!("matched -> {y}");

    // Ignore
    let mut _k = SomeKind::Foo;
    _k = SomeKind::Bar;


}
