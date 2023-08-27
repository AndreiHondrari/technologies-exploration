#[allow(dead_code)]
mod some {
    struct Foo {}

    pub struct Bar {}

    pub enum Kind {
        Rose,
        Thunder,
    }

    pub struct Kek {
        pub a: u16,
        b: u32,
    }

    // necessary to implement a new
    // function to construct Kek
    // because b is private
    impl Kek {
        pub fn new(a: u16, b: u32) -> Self {
            Kek { a, b }
        }
    }
}

fn main() {
    // NOTICE - Foo is private
    // let a = some::Foo;
    let _x = some::Bar {};
    let _x = some::Kind::Thunder;

    // NOTICE - b is private
    // let x = some::Kek { a: 11, b: 22 };
    let _x = some::Kek::new(11, 22);
}
