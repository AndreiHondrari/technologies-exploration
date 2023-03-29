
use std::fmt::Display;

struct Something {}

impl Something {

    fn do_some<T: Display>(&self, k: T)
    {
        println!("{k}");
    }
}


fn main() {
    let s1 = Something{};
    s1.do_some(123);
}
