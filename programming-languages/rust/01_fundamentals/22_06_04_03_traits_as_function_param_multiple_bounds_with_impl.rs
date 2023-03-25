/*
generics - traits - as function parameters - bound multiple times with impl
*/

// declare some structs

#[derive(Copy, Clone)]
struct Foo;

// declare traits - common behaviour interface
trait TraitKek {
    fn do_some(&self);
}

trait TraitPop {
    fn do_else(&self);
}

// implement behaviour for structs
impl TraitKek for Foo {
    fn do_some(&self) {
        println!("Foo | do_some");
    }
}

impl TraitPop for Foo {
    fn do_else(&self) {
        println!("Foo | do_else");
    }
}

// function using trait as param
fn do_this(x: impl TraitKek + TraitPop) {
    x.do_some();
    x.do_else();
}

fn do_that(x: &(impl TraitKek + TraitPop)) {
    x.do_some();
    x.do_else();
}


fn main() {
    let x = Foo {};

    println!("\n{}", "do this");
    do_this(x);

    println!("\n{}", "do that");
    do_that(&x);
}
