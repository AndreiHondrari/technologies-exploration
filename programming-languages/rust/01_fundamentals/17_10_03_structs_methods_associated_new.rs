/*
Structs - associated 'new' methods

Methods that can be constructors
*/


fn main() {

    struct Thing {
        a: u32
    }

    impl Thing {
        fn make_this() -> Self {
            Self {a: 11}
        }

        fn make_that() -> Thing {
            Thing {a: 22}
        }
    }

    let x = Thing::make_this();
    println!("{}", x.a);

    let y = Thing::make_that();
    println!("{}", y.a);

}
