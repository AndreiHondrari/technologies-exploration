/*
Structs - methods

Methods can alter attributes on
the current instance, only if
self is declared as a mutable reference,
and the instance is declared mutable.
*/


fn main() {

    struct Thing {
        a: u32
    }

    impl Thing {
        // NOTICE the '&mut self'
        fn alter_inside(&mut self) {
            self.a = 22;
        }
    }

    // NOTICE the 'mut'
    let mut x = Thing {a: 11};
    println!("before -> {}", x.a);

    // call affecting method
    x.alter_inside();

    println!("after  -> {}", x.a);

}
