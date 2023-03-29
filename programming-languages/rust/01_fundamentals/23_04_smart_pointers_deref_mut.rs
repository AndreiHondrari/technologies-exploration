/*
smart pointers - dereferencing mutable
*/

use std::ops::Deref;
use std::ops::DerefMut;

struct Something {
    x: u16,
    y: u16
}

// this is necessary
// because DerefMut is bound by Deref
impl Deref for Something {
    type Target = u16;

    fn deref(&self) -> &Self::Target {
        &self.x
    }
}

// Target comes from Deref
// hence it is not needed to respecify here
impl DerefMut for Something {
    fn deref_mut(&mut self) -> &mut Self::Target {
        &mut self.x
    }
}

fn main() {
    let mut s1 = Something {x: 123, y: 777};

    println!("BEF {}", *s1);

    *s1 = 999;

    println!("AFT {}", *s1);

    // ignore
    let _i = s1.y;
}
