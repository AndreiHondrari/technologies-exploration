/*
Move from reference - impossible - compile error
*/

#[allow(dead_code)]
#[derive(Debug)]
struct Foo {
    val: u16,
}

fn main() {
    let a = Foo { val: 123 };

    let x = &a;

    let p = *x;

    println!("{p:?}");
}
