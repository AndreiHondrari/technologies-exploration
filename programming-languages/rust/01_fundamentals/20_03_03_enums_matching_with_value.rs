/*
Enums - pattern matching - use value
*/

#[derive(Debug)]
enum SomeKind {
    Foo(u32),
    Bar {a: u32},
}

fn choose(kind: SomeKind) {
    match kind {
        SomeKind::Foo(value) => {
            println!("AAA {}", value);
        },

        SomeKind::Bar{a} => {
            println!("BBB {}", a);
        },
    };
}

fn main() {
    choose(SomeKind::Foo(123));
    choose(SomeKind::Bar{a: 777});
}
