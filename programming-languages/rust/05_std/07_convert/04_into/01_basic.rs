/*
Into - basic

into() is an instance bound conversion method.
Into is implemented for converting internal types into external types.
(assuming ExternalThing exists outside this crate)

Suitable for implicit conversion.
*/

use std::convert::Into;

#[allow(dead_code)]
#[derive(Debug)]
struct ExternalThing {
    k: i8,
}

#[derive(Debug, Clone)]
struct InternalThing {
    p: u16,
}

impl Into<ExternalThing> for InternalThing {
    fn into(self) -> ExternalThing {
        ExternalThing { k: self.p as i8 }
    }
}

fn main() {
    let internal_thing = InternalThing { p: 123 };
    println!("internal_thing {:?}", internal_thing);

    let external_thing: ExternalThing = internal_thing.clone().into();
    println!("external_thing #1 {:?}", external_thing);

    let external_thing = Into::<ExternalThing>::into(internal_thing.clone());
    println!("external_thing #2 {:?}", external_thing);
}
