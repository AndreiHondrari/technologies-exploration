/*
Enums - pattern matching - match specific value - COMPILATION ERROR

If the match all entry is not present, the compiler will complain.
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
        // _ => {}
    };
}

fn main() {
    choose(SomeKind::Foo(111));
    choose(SomeKind::Foo(222));
    choose(SomeKind::Foo(333));
}
