/*
Into - implicitly caused by From implementation

Implementing From means that

foo = Foo::from(bar)

which means that there is an implicit into()

foo: Foo = bar.into()  -> reuses the From implementation

*/
use std::convert::{From, Into};

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

    /*
    Observe the original from() usage.

    let internal_thing = InternalThing::from(external_thing);
    */
    let internal_thing: InternalThing = external_thing.into();
    println!("{:?}", internal_thing);
}
