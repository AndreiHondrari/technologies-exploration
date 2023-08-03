/*
Polymorphism - ad-hoc

Function overloading is not possible in rust
therefore we must use generics and traits
*/

trait Special {
    fn do_some(&self);
}

impl Special for u16 {
    fn do_some(&self) {
        println!("do AAA");
    }
}

impl Special for u32 {
    fn do_some(&self) {
        println!("do BBB");
    }
}

fn do_some<T: Special>(x: T) {
    x.do_some();
}

fn main() {
    let a: u16 = 111;
    let b: u32 = 222;

    do_some(a);
    do_some(b);
}
