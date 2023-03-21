/*
generics - traits - as function parameters
*/

// declare some structs

#[derive(Copy, Clone)]
struct Foo;

#[derive(Copy, Clone)]
struct Bar;

// declare trait - common behaviour interface
trait Some {
    fn do_some(&self);
}

// implement behaviour for structs
impl Some for Foo {
    fn do_some(&self) {
        println!("Foo | do_some");
    }
}

impl Some for Bar {
    fn do_some(&self) {
        println!("Bar | do_some");
    }
}

// function using trait as param
fn do_this(x: impl Some) {
    x.do_some();
}

fn do_that(x: &impl Some) {
    x.do_some();
}


fn main() {
    let s1 = Foo {};
    let s2 = Bar {};

    println!("\n{}", "do this");
    do_this(s1);
    do_this(s2);

    println!("\n{}", "do that");
    do_that(&s1);
    do_that(&s2);
}
