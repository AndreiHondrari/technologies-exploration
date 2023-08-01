/*
Structs - Copy

Copy means "move" which is still copy in the background,
but with the added benefit of being able to access the first variable.
*/

/*
The copy and clone traits turn this struct into a copy-able one
*/
#[derive(Debug, Clone, Copy)]
struct Foo {
    x: u16,
}

fn main() {
    let mut a = Foo { x: 111 };
    println!("a before: \t{a:?}");

    let b = a; // this is a copy

    a.x = 222; // you can still use the original from a

    println!("a after:\t{a:?}");
    println!("b:\t\t{b:?}");
}
