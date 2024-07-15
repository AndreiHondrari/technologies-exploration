/*
generics - associated types - multiple associated types
*/

struct Something {}

trait SomeTrait {
    type Foo;
    type Bar;

    fn do_some(&self) -> (Self::Foo, Self::Bar);
}

impl SomeTrait for Something {
    type Foo = u32; // THIS IS REQUIRED
    type Bar = f32; // THIS IS REQUIRED

    fn do_some(&self) -> (Self::Foo, Self::Bar) {
        (123, 3.14)
    }
}

fn main() {
    let s1: Something = Something {};

    let k = s1.do_some();
    println!("{k:?}");
}
