/*
Polymorphism - subtyping

Struct inheritance does not exist but trait extension does.
Notice you are forced to implement the base trait
for all the structs that are intended for use as a base trait structure.

In any case the form/shape/implementation of the subtraits
are irrelevant when passing the structures as base trait
to a function. Traits are not types
*/

trait BaseTrait {
    fn do_this(&self);
}

trait SubtraitA: BaseTrait {}

trait SubtraitB: BaseTrait {}

//
struct Foo {}

impl BaseTrait for Foo {
    fn do_this(&self) {
        println!("do AA");
    }
}

impl SubtraitA for Foo {}

//
struct Kek {}

impl BaseTrait for Kek {
    fn do_this(&self) {
        println!("do BB");
    }
}

impl SubtraitB for Kek {}

fn do_some<T: BaseTrait>(x: T) {
    x.do_this();
}

fn main() {
    let foo = Foo {};
    let kek = Kek {};

    do_some(foo);
    do_some(kek);
}
