/*
Traits - Conditional implementation of trait for a generic

impl<T: SomeBound> SomeTrait for T

will attach SomeTrait functionality to any type that
implements SomeBound, without particularly specifying it for
that type.

The downside is that you can't use attributes defined
on that type from self, because they are not determinable.
*/

// a trait used for conditional bounds
trait TraitKek {
    fn do_kek(&self);
}

// conditional implementation for generic
trait TraitMain {
    fn do_special(&self);
}

impl<T: TraitKek> TraitMain for T {
    fn do_special(&self) {
        println!("do_special PRE");
        self.do_kek();
        println!("do_special POST");
    }
}


// type and implementation for conditional behaviour
struct Foo {name: String}
// struct Bar;

impl TraitKek for Foo {
    fn do_kek(&self) {
        println!("{} does kek", self.name);
    }
}


fn main() {
    let foo = Foo {name: String::from("FooInstance")};
    foo.do_special();
}
