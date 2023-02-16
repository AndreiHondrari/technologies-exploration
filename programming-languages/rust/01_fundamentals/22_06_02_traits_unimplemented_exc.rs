/*
generics - traits - compile error for unimplemented methods
*/

// declare some structs
struct Foo {}

// declare trait - common behaviour interface
trait Some {
    fn do_some(&self) -> u32;
}

// implement behaviour for structs
impl Some for Foo {
    // NOTICE do_some is not implemented here
    // fn do_some(&self) -> u32 {}
}


fn main() {
    let _o = Foo {};
}
