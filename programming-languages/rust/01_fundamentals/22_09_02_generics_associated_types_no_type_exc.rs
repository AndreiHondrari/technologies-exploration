/*
generics - associated types - not specifying the type - EXCEPTION
*/

struct Something {}

trait SomeTrait {
    type Placeholder;

    fn do_some(&self) -> Self::Placeholder;
}

impl SomeTrait for Something {
    // INTENTIONALLY: not defining the Placeholder type
    // type Placeholder = u32;  // WILL NOT WORK

    fn do_some(&self) -> Self::Placeholder {
        123
    }
}

fn main() {
    let s1: Something = Something {};

    let k = s1.do_some();
    println!("{k}");
}
