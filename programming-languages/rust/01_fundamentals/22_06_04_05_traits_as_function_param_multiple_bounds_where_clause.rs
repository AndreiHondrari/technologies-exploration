/*
generics - traits - as function parameters - where clause for de-cluttering
*/

// declare some structs

#[derive(Copy, Clone)]
struct Foo;

#[derive(Copy, Clone)]
struct Bar;

// declare traits - common behaviour interface
trait TraitKek {
    fn do_some(&self);
}

trait TraitPop {
    fn do_else(&self);
}

trait TraitWat {
    fn do_wat(&self);
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

impl TraitWat for Bar {
    fn do_wat(&self) {
        println!("Bar | do_wat");
    }
}

// function using trait as param
fn do_this<T, U>(x: T, y: U)
where
    T: TraitKek + TraitPop,
    U: TraitWat,
{
    x.do_some();
    x.do_else();
    y.do_wat();
}

fn do_that<T, U>(x: &T, y: &U)
where
    T: TraitKek + TraitPop,
    U: TraitWat,
{
    x.do_some();
    x.do_else();
    y.do_wat();
}


fn main() {
    let x = Foo {};
    let y = Bar {};

    println!("\n{}", "do this");
    do_this(x, y);

    println!("\n{}", "do that");
    do_that(&x, &y);
}
