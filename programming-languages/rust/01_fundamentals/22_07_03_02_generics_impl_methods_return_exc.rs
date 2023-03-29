/*
generics - impl - methods - return type

Sample will throw a compilation error
because T is not bound by the Copy trait
and the compiler does not know how to
handle returning a value of type T
*/

struct Something<T> {
    x: T
}

impl<T> Something<T>
// NOTICE: we don't bound T by copy
// where
//     T: Copy
{

    fn do_some(&self) -> T {
        self.x
    }
}


fn main() {
    let s1: Something<u32> = Something{x: 123};
    let k: u32 = s1.do_some();
    println!("{k}");
}
