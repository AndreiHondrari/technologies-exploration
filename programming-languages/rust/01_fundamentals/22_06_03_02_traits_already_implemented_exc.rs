/*
generics - traits - compile error for already implemented trait

Let's say we wanted to split the implementation of a trait
in two separate blocks. This is not possible.

If we want to split functionality then our problem is
granularity of the trait itself. Most likely we
are looking at two distinct traits.
*/

// declare some structs
struct Foo {}

// declare trait - common behaviour interface
trait Some {
    fn do_some(&self);
    fn do_that(&self);
}

// split implement behaviour for structs
impl Some for Foo {
    fn do_some(&self) {
        println!("do some");
    }
}

// this will not work
impl Some for Foo {
    fn do_that(&self) {
        println!("do that");
    }
}

fn main() {
    let _o = Foo {};
}
