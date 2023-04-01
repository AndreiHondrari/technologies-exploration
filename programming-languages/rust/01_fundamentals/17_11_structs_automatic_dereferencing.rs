/*
Structs - automatic dereferencing

In other programming languages,
when trying to access the inner implementation
through a pointer or a reference,
one would have to use the '->' operator.

In Rust, references & pointers are automatically
dereferenced when using the '.' accessor.
*/


fn main() {

    struct Thing;

    // notice one impl
    impl Thing {
        fn do_this(&self) {
            println!("Doing this");
        }
    }

    // make an instance
    let x = Thing;

    // reference the instance
    let y: &Thing = &x;

    // use it with manual dereferencing
    (*y).do_this();

    // use with automatic dereferencing
    y.do_this();
}
