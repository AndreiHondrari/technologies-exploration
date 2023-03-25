/*
generics - traits - as function parameters but by generically bounding
*/

// declare some structs

#[derive(Copy, Clone)]
struct Foo;

// declare trait - common behaviour interface
trait TraitKek {
    fn do_some(&self);
}

// implement behaviour for structs
impl TraitKek for Foo {
    fn do_some(&self) {
        println!("Foo | do_some");
    }
}

// function using trait as param
fn do_this<T: TraitKek>(x: T) {
    x.do_some();
}

fn do_that<T: TraitKek>(x: &T) {
    x.do_some();
}


fn main() {
    let x = Foo {};

    println!("\n{}", "do this");
    do_this(x);

    println!("\n{}", "do that");
    do_that(&x);
}
