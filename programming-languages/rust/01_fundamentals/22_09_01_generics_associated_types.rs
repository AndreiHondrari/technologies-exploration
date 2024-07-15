/*
generics - associated types
*/

struct Something {}

trait SomeTrait {
    type Placeholder;

    fn do_some(&self) -> Self::Placeholder;
}

impl SomeTrait for Something {
    type Placeholder = u32; // THIS IS REQUIRED

    fn do_some(&self) -> Self::Placeholder {
        123
    }
}

fn main() {
    let s1: Something = Something {};

    let k = s1.do_some();
    println!("{k}");
}
