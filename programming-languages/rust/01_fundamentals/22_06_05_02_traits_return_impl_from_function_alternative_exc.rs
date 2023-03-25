/*
generics - traits - return from function multiple alternative structs implementing trait
throws exception because compiler does not allow it.
there are other ways to return alternative structs from a function.
*/

// declare some structs

#[derive(Copy, Clone)]
struct Foo;

#[derive(Copy, Clone)]
struct Bar;

// declare traits - common behaviour interface
trait TraitKek {
    fn do_some(&self) { println!("Whatever"); };
}

// implement behaviour for structs
impl TraitKek for Foo {};
impl TraitKek for Bar {};

// functions returning alternative structs implementing trait
fn give_this(is_stuff: bool) -> impl TraitKek
{
    if (is_stuff) {
        return Foo {};
    } else {
        return Bar {};  // will not be allowed by compiler
    };
}


fn main() {
    // Notice that trying to annotate x with 'impl TraitKek'
    // does not really work

    let x = give_this(true);
    x.do_some();

    x = give_this(false);
    x.do_some();
}
