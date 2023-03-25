/*
generics - traits - compile error for unimplemented methods
*/

// declare some structs
struct Foo;

// declare trait - common behaviour interface
trait Some {
    fn do_some(&self) -> u32 {
        println!("Some | default do_some");
        123
    }
}

// implement behaviour for structs
impl Some for Foo {
    // NOTICE do_some is not implemented here
}


fn main() {
    let o = Foo {};
    let x = o.do_some();
    println!("{x}");
}
