/*
traits - subtyping unimplemented subtype conflicting method
*/

// define traits
trait MegaTrait {
    fn do_mega(&self);
}

trait LameTrait: MegaTrait {
    fn do_lame(&self);
    fn do_mega(&self);
}

struct Foo;

impl MegaTrait for Foo {
    fn do_mega(&self) {
        println!("do_mega");
    }
}

impl LameTrait for Foo {
    fn do_lame(&self) {
        println!("do_lame");
    }

    /*
    <-- NOTICE LACK OF do_mega
    compiled will fail here
    because there is no inheritance
    in Rust
    */
}

fn main() {}
