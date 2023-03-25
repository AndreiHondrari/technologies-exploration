/*
generics - traits - compile error for conflicting methods from different traits


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

    // WILL NOT WORK
    // do_some is defined in both TraitA and TraitB
    foo.do_some();
}
