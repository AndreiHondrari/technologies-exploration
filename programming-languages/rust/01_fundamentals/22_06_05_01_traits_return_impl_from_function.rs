/*
generics - traits - return from function structs implementing trait
*/

// declare some structs

#[derive(Copy, Clone)]
struct Foo;

// declare traits - common behaviour interface
trait TraitKek {
    fn do_some(&self);
}

// implement behaviour for structs
impl TraitKek for Foo {
    fn do_some(&self) {
        println!("Foo | do_some");
    }
}

// functions returning struct implementing trait
fn give_this() -> impl TraitKek
{
    return Foo {};
}


fn main() {
    // Notice that trying to annotate x with 'impl TraitKek'
    // does not really work
    let x = give_this();
    println!("\n{}", "after return");
    x.do_some();
}
