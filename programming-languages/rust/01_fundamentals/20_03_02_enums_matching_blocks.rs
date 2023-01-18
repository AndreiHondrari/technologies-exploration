/*
Enums - pattern matching - code blocks
*/


fn main() {

    #[derive(Debug)]
    enum SomeKind {Foo, Bar, Kek}

    let x = SomeKind::Kek;
    println!("defined -> {:?}", x);

    match x {
        SomeKind::Foo => {
            println!("AAA");
        },

        SomeKind::Bar => {
            println!("BBB");
        },

        SomeKind::Kek => {
            println!("CCC");
        },
    };

    // Ignore
    let mut _k = SomeKind::Foo;
    _k = SomeKind::Bar;


}
