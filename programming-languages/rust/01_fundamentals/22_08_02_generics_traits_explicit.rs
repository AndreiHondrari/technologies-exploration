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

    let k = <Something as SomeTrait<u32>>::do_some(&s1, 123);
    println!("k as String: `{k}`");
}
