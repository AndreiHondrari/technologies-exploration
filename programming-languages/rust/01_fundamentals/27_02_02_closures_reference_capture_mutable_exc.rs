/*
Functions - Closures

Mutating a variable that was borrowed by a closure results in compilation error
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

    let mut my_func = || x.give_some(); // borrows x as reference

    let k = my_func(); // uses the reference of x
    println!("{k}");

    x = Foo { a: 1000 }; // x changed here -> CAUSES COMPILE ERROR

    let p = my_func(); // uses the reference of x
    println!("{p}");

    println!("{x:?}");
}
