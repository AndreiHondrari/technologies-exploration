/*
AsRef - basic
*/

use std::convert::AsRef;

struct Foo<'xlife> {
    x_ref: &'xlife u16,
}

impl AsRef<u16> for Foo<'_> {
    fn as_ref(&self) -> &u16 {
        self.x_ref
    }
}

fn main() {
    let x: u16 = 123;

    let foo = Foo { x_ref: &x };

    let y: &u16 = foo.as_ref();

    println!("y {}", y);
}
