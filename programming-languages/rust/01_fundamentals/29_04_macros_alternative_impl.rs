/*
Macros - alternative implementation
*/

macro_rules! lay_some_impl {
    (foo) => {
        impl Some {
            fn do_this(self) {
                println!("AAAAA");
            }
        }
    };

    (bar) => {
        impl Some {
            fn do_this(self) {
                println!("BBBBB");
            }
        }
    };
}

#[derive(Debug)]
struct Some {}

lay_some_impl!(bar);

fn main() {
    let x = Some {};

    x.do_this();
}
