/*
Functions - Closures

Closures can capture variables from outside by value by using the keyword 'move'
*/

#[allow(dead_code)]
#[derive(Debug)]
struct Foo {
    a: u16,
}

impl Foo {
    fn give_some(&mut self) -> u16 {
        self.a += 1;
        self.a
    }
}

fn main() {
    let mut x = Foo { a: 1 };

    let mut my_func = move || x.give_some(); // x is transferred to the closure

    // x no longer usable here because it was moved in the closure
    // if used -> compilation error
    // println!("{x:?}");

    let k = my_func(); // uses the moved x
    println!("{k}");

    x = Foo { a: 1000 }; // x reassigned is alright here, x will just point to this new memory

    let p = my_func(); // uses the moved x
    println!("{p}");

    println!("{x:?}");
}
