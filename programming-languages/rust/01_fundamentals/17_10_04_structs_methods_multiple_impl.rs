/*
Structs - multiple impl blocks

Methods that can split between multiple
impl blocks
*/


fn main() {

    struct Thing;

    // notice one impl
    impl Thing {
        fn do_this(&self) {
            println!("Doing this");
        }
    }

    // notice second impl
    impl Thing {
        fn do_that(&self) {
            println!("Doing that");
        }
    }

    let x = Thing;
    x.do_this();
    x.do_that();

}
