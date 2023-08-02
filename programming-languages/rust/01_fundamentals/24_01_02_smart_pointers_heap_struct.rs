/*
smart pointers - heap - structs
*/

#[allow(dead_code)]
#[derive(Debug)]
struct Foo {
    x: u16,
}

fn main() {
    let x: Box<Foo> = Box::new(Foo { x: 123 });

    println!("{x:?}");
}
