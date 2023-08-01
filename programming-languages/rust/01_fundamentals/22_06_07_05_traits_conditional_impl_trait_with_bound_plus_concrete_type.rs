/*
Traits - Conditional implementation of trait + concrete implementation

If we have a conditional generic implementation,
we can still implement that conditionally used trait
for a concrete type, unconditionally.

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

// unconditional implementation for a concrete type
impl TraitMain for Something<u32> {
    fn do_special(&self) {
        println!("{} calling extra special for u32", self.name);
    }
}

// type and implementation for conditional behaviour
struct Foo {substruct_name: String}

impl TraitKek for Foo {
    fn do_kek(&self) {
        println!("{} does kek", self.substruct_name);
    }
}


fn main() {
    let foo = Foo {substruct_name: String::from("FooInstance")};

    let s1: Something<Foo> = Something {
        name: String::from("S1_foo"),
        x: foo
    };

    // notice that the conditional behaviour is not relevant here
    // s2 will have a different do_special, specifically defined for u32
    let s2: Something<u32> = Something {
        name: String::from("S2_u32"),
        x: 123u32
    };

    s1.do_something();
    s2.do_something();

    s1.do_special();
    s2.do_special();
}
