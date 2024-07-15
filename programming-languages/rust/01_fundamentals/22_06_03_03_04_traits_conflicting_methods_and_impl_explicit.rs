/*
generics - traits - conflicting between traits and impl

If the same method is defined in multiple traits and an impl block,
rust will call the impl as default, unless otherwise specifically called.
*/

// declare some structs
struct Foo {}

impl Foo {
    fn do_some(&self) {
        println!("do some but main impl");
    }
}

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

    foo.do_some(); // will choose the impl definition
    TraitB::do_some(&foo);
}
