/*
Structs - unit like

Struct without data
*/

fn main() {
    struct Foo; // Notice no data definition

    #[allow(unused_variables)] // to silence the compiler about lack of use
    let x = Foo;
}
