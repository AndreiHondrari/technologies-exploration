/*
smart pointers - dereferencing custom
*/

use std::ops::Deref;

struct Something {
    x: u16,
    y: u16
}

impl Deref for Something {
    type Target = u16;

    fn deref(&self) -> &Self::Target {
        &self.x
    }
}

fn main() {
    let s1 = Something {x: 123, y: 777};

    let k: u16 = *s1;
    println!("{}", k);

    // ignore
    let _i = s1.y;
}
