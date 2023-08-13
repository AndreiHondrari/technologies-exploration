/*
Destructure references of structs
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

    // a and b references are used for the tuple (&a, &b)
    let (x, y): (&Foo, &Foo) = (&a, &b);

    println!("{x:?} | {y:?}");

    let _k = a;
    let _p = b;
}
