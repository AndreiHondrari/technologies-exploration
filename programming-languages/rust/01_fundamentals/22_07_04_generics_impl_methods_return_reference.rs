/*
generics - methods - return type - as reference
*/

struct Something<T> {
    x: T
}

impl<T> Something<T> {

    fn do_some(&self) -> &T {
        &self.x
    }
}


fn main() {
    let s1: Something<u32> = Something{x: 123};
    let k: &u32 = s1.do_some();
    println!("{k}");
}
