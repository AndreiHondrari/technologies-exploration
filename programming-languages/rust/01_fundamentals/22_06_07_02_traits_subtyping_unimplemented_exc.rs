/*
traits - subtyping - supertrait not implemented on purpose

Not implementing a supertrait required by a subtrait will
result in a compilation error.
*/


// define traits
trait MegaTrait {
    fn do_mega(&self);
}

trait LameTrait : MegaTrait {
    fn do_lame(&self);
}

// define structs
struct Something {
    x: u16
}

// implement mega trait for structs

// NOTICE: NOT IMPLEMENTED BY PURPOSE
// impl MegaTrait for Something {}

// implement subtraits for structs
// will not work
// compile will fail because LameTrait requires MegaTrait implementation
impl LameTrait for Something {
    fn do_lame(&self) {
        println!("Something LameTrait do_lame {}", self.x);
    }
}

fn main() {
    let s = Something{x: 111};
    s.do_mega();
    s.do_lame();
}
