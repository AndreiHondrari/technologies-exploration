/*
Enums - pattern matching - match specific value
*/

#[derive(Debug)]
enum SomeKind {
    Foo(u32),
}

fn choose(kind: SomeKind) {
    match kind {
        SomeKind::Foo(222) => {
            println!("--- 222 MATCHED ---");
        }
        other => {
            println!("Other {:?}", other);
        }
    };
}

fn main() {
    choose(SomeKind::Foo(111));
    choose(SomeKind::Foo(222));
    choose(SomeKind::Foo(333));
}
