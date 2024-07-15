/*
generics - associated types
*/

struct Something {}

trait SomeTrait<T> {
    fn do_some(&self, val: T) -> String;
}

impl<T: ToString> SomeTrait<T> for Something {
    fn do_some(&self, val: T) -> String {
        val.to_string()
    }
}

fn main() {
    let s1: Something = Something {};

    let k = s1.do_some(123);
    println!("k as String: `{k}`");
}
