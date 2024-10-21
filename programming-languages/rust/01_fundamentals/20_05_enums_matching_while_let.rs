/*
Enums pattern matching - while let

Instead of breaking the loop
due to unmatched conditions

loop {
    match x {
        123 => { do_this() },
        _ => { break; }
    }
}

we can instead use 'while let'

works only with enums
*/

#[derive(Debug)]
enum SomeKind {
    Foo,
    Bar,
}

fn choose(kind: SomeKind) {
    println!("kind -> {:?}", kind);

    let mut i: u8 = 0;
    while let SomeKind::Foo = kind {
        i += 1;
        if i >= 4 { break ;};
        println!("N {i}");
    }
}

fn main() {
    choose(SomeKind::Foo);
    choose(SomeKind::Bar);
}
