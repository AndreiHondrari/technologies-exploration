/*
Enums pattern matching - if let

Instead of matching only
one value with alternative as:

match x {
    123 => { do_this() },
    _ => do_else()
}

it can be replaced with 'if let else'.

works only with enums
*/

#[derive(Debug)]
enum SomeKind {
    Foo,
    Bar,
    Kek
}

fn choose(kind: SomeKind) {
    if let SomeKind::Bar = kind {
        println!("the one and only {kind:?}");
    } else {
        println!("other {kind:?}");
    };
}

fn main() {
    choose(SomeKind::Foo);
    choose(SomeKind::Bar);
    choose(SomeKind::Kek);
}
