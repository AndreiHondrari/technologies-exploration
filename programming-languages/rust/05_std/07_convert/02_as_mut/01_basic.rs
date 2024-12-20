/*
AsMut - basic
*/

use std::convert::AsMut;

struct Foo<'xlife> {
    x_ref: &'xlife mut u16,
}

impl AsMut<u16> for Foo<'_> {
    fn as_mut(&mut self) -> &mut u16 {
        self.x_ref
    }
}

fn main() {
    let mut x: u16 = 123;
    println!("x before mutation:    {}", x);

    let mut foo = Foo { x_ref: &mut x };

    let y: &mut u16 = foo.as_mut();

    *y = 777;

    println!("x after mutation:     {}", x);
}
