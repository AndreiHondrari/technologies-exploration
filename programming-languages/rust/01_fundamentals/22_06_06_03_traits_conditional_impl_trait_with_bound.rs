/*
Traits - Conditional implementation of trait for struct with trait bounds

By using trait bounds with impl trait blocks we practically
limit which entities get specific methods or not.
*/

// a trait used for conditional bounds

trait TraitKek {
    fn do_kek(&self);
}

// trait for structure

trait TraitMain {
    fn do_special(&self);
}

// our main structure
struct Something<T> {
    name: String,
    x: T
}

impl<T> Something<T> {
    fn do_something(&self) {
        println!("{} does something", self.name);
    }
}

// conditional implementation for main struct
impl<T: TraitKek> TraitMain for Something<T> {
    fn do_special(&self) {
        println!("{} do_special PRE", self.name);
        self.x.do_kek();
        println!("{} do_special POST", self.name);
    }
}

// sub structures affecting the implementation of the main struct
struct Foo {substruct_name: String}
struct Bar {}

// attach TraitKek impl to Bar
// to distinguish it from Foo
impl TraitKek for Foo {
    fn do_kek(&self) {
        println!("{} does kek", self.substruct_name);
    }
}


fn main() {
    let foo = Foo {substruct_name: String::from("FooInstance")};
    let bar = Bar {};

    let s1: Something<Foo> = Something {
        name: String::from("S1_foo"),
        x: foo
    };

    let s2: Something<Bar> = Something {
        name: String::from("S2_bar"),
        x: bar
    };

    s1.do_something();
    s2.do_something();

    // the following works because do_special is
    // attached to the s1 entity, since it was initialized
    // with a substruct (Foo) that implements TraitKek
    s1.do_special();

    // alternatively s2 was initialized with a substruct (Bar)
    // that does not implement TraitKek, so the impl bound
    // will prevent from adding do_special to it
    // s2.do_special();  // WILL NOT WORK
}
