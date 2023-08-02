/*
Functions - Closures

Closures by default borrow variables from outside their scope as a reference
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

    let p = my_func(); // uses the reference of x
    println!("{p}");

    println!("{x:?}");
}
