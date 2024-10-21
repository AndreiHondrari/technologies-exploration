/*
traits - referencing entities that implement a specific trait

'dyn Struct' can not be used as a direct type
because it wouldn't make sense to copy a structure
that has dynamic size.

With references it works because rust uses a virtual dispatch table
which keeps pointers to actual implementations of methods.
*/

// declare trait - common behaviour interface
trait Some {
    fn do_some(&self);
}

// declare some structs
struct Foo {
    x: u32,
}

struct Bar {
    y: u16,
}

// implement behaviour for structs
impl Some for Foo {
    fn do_some(&self) {
        println!("SomeFoo do_some {}", self.x);
    }
}

impl Some for Bar {
    fn do_some(&self) {
        println!("SomeBar do_some {}", self.y);
    }
}

fn main() {
    let foo = Foo { x: 111 };
    let bar = Bar { y: 222 };

    // Notice k can take any reference that implements a specific trait
    let mut k: &dyn Some = &foo;
    k.do_some();

    k = &bar;
    k.do_some();
}
