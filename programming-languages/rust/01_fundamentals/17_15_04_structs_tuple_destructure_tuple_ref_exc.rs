/*
Destructure reference tuple of structs - show compile error
*/

#[allow(dead_code)]
#[derive(Debug)]
struct Foo {
    val: u16,
}

fn main() {
    let a = Foo { val: 11 };
    let b = Foo { val: 22 };

    println!("{a:?} | {b:?}");

    // a and b are moved into the tuple (a, b)
    let (x, y): &(Foo, Foo) = &(a, b); // the reference is to the tuple

    println!("{x:?} | {y:?}");

    // WILL NOT WORK because a and b are moved into the tuple (a, b)
    // let _k = a;
    // let _p = b;
}
