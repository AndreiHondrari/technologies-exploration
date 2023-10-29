/*
From - basic

from() is a constructor kind of conversion method (unbound to instance).
From is implemented for converting external types into internal types.
(assuming ExternalThing exists outside this crate)

Suitable for explicit conversion.
*/

use std::convert::From;

#[derive(Debug, Clone)]
struct ExternalThing {
    k: i8,
}

#[allow(dead_code)]
#[derive(Debug)]
struct InternalThing {
    p: u16,
}

impl From<ExternalThing> for InternalThing {
    fn from(value: ExternalThing) -> Self {
        InternalThing { p: value.k as u16 }
    }
}

fn main() {
    let external_thing = ExternalThing { k: 123 };
    println!("external_thing {:?}", external_thing);

    let internal_thing = InternalThing::from(external_thing);
    println!("internal_thing {:?}", internal_thing);
}
