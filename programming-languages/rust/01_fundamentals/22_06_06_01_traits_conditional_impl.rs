/*
Traits - Conditional implementation of struct with trait bounds

By using trait bounds with impl blocks we practically
limit which entities get specific methods or not.
*/

// a trait used for conditional bounds

trait TraitKek {
    fn do_kek(&self);
}

// our main structure
struct Something<T> {
    name: String,
    x: T
}

// default implementation for main struct
// the <T> is required for impl
// so that we have available for the struct
impl<T> Something<T> {
    fn do_something(&self) {
        println!("{} does something", self.name);
    }
}

// conditional implementation for main struct
impl<T: TraitKek> Something<T> {
    fn do_special(&self) {
        println!("{} do_special PRE", self.name);
        self.x.do_kek();
        println!("{} do_special PPOST", self.name);
    }
}

// sub structures affecting the implementation of the main struct
struct Foo {}
struct Bar {substruct_name: String}

// attach TraitKek impl to Bar
// to distinguish it from Foo
impl TraitKek for Bar {
    fn do_kek(&self) {
        println!("{} does kek", self.substruct_name);
    }
}


fn main() {
    let foo = Foo {};
    let bar = Bar {substruct_name: String::from("BarInstance")};

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
    // attached to the s2 entity, since it was initialized
    // with a substruct (Bar) that implements TraitKek
    s2.do_special();

    // alternatively s1 was initialized with a substruct (Foo)
    // that does not implement TraitKek, so the impl bound
    // will prevent from adding do_special to it
    // s1.do_special  // WILL NOT WORK
}
