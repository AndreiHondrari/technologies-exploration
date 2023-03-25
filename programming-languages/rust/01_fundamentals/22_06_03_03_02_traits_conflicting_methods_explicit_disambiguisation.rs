/*
generics - traits - explicit disambiguisation calls from traits
that are implementing the same method signature.
*/

// declare some structs
struct Foo {}

// declare conflicting trait (notice they both have do_some)
trait TraitA {
    fn do_some(&self);
}

trait TraitB {
    fn do_some(&self);
}

impl TraitA for Foo {
    fn do_some(&self) {
        println!("do some A");
    }
}

impl TraitB for Foo {
    fn do_some(&self) {
        println!("do some B");
    }
}

fn main() {
    let foo = Foo {};

    // call from each trait separately
    TraitA::do_some(&foo);
    TraitB::do_some(&foo);
}
