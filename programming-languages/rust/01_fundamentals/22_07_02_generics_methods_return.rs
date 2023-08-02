/*
generics - methods - return type
*/

struct Something;

impl Something {
    fn get_some<T>(&self, x: T) -> T {
        x
    }
}

fn main() {
    let s1 = Something {};
    let k: u32 = s1.get_some(123);
    println!("{k}");
}
