/*
Structs - methods

self is a reference to the current instance.
'&self' is a shortcut to 'self: &Self'
declaring '&self' means it is immutable.
*/


fn main() {

    struct Thing {
        a: u32,
        b: u32
    }

    impl Thing {
        fn do_this(&self) -> u32 {
            self.a + self.b
        }

        fn do_that(self: &Self) -> u32 {
            (self.a + self.b) * 11
        }
    }

    let x = Thing {a: 11, b: 22};
    println!("x.do_this() -> {}", x.do_this());
    println!("x.do_that() -> {}", x.do_that());

}
