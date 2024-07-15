/*
Structs - methods

If a struct has a method that expects a mutable self,
trying to call that method while the struct instance
is declare as immutable, results in a borrow violation.
*/

fn main() {
    struct Thing {
        a: u32,
    }

    impl Thing {
        // NOTICE the '&mut self'
        fn alter_inside(&mut self) {
            self.a = 22;
        }
    }

    // OBSERVATION -> x is immutable -> affects borrowing for alter_inside call
    let x = Thing { a: 11 };
    println!("before -> {}", x.a);

    // call affecting method
    x.alter_inside(); // <-- WILL NOT WORK!

    println!("after  -> {}", x.a);
}
