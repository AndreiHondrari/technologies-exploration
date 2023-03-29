/*
traits - subtyping

*/


// define traits
trait MegaTrait {
    fn do_mega(&self);
}

trait LameTrait : MegaTrait {
    fn do_lame(&self);
}

// define structs
struct A {
    x: u16
}

struct B {
    y: u32
}

// implement mega trait for structs

impl MegaTrait for A {
    fn do_mega(&self) {
        println!("A MegaTrait do_mega {}", self.x);
    }
}

impl MegaTrait for B {
    fn do_mega(&self) {
        println!("B MegaTrait do_mega {}", self.y);
    }
}

// implement subtraits for structs

impl LameTrait for A {
    fn do_lame(&self) {
        println!("A LameTrait do_lame {}", self.x);
    }
}

impl LameTrait for B {
    fn do_lame(&self) {
        println!("B LameTrait do_lame {}", self.y);
    }
}

fn main() {
    let a = A{x: 111};
    a.do_mega();
    a.do_lame();

    let b = B{y: 222};
    b.do_mega();
    b.do_lame();
}
