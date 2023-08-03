/*
Polymorphism - ad-hoc

Instead of defining the special behaviour directly on the type,
we can wrap the type in a generic struct so the functionality is contained
*/

#[allow(dead_code)]
struct Wrapped<T> {
    number: T,
}

trait Special {
    fn do_some(&self);
}

impl Special for Wrapped<u16> {
    fn do_some(&self) {
        println!("do AAA");
    }
}

impl Special for Wrapped<u32> {
    fn do_some(&self) {
        println!("do BBB");
    }
}

fn do_some<T: Special>(x: T) {
    x.do_some();
}

fn main() {
    let a: Wrapped<u16> = Wrapped { number: 111 };
    let b: Wrapped<u32> = Wrapped { number: 222 };

    do_some(a);
    do_some(b);
}
