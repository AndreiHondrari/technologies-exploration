/*
generics - impl - methods - return type
*/

struct Something<T> {
    x: T
}

// NOTICE: T must be bounds by Copy trait
// so that the method can return the value
impl<T: Copy> Something<T> {

    fn do_some(&self) -> T {
        self.x
    }
}


fn main() {
    let s1: Something<u32> = Something{x: 123};
    let k: u32 = s1.do_some();
    println!("{k}");
}
