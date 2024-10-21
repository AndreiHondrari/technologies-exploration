/*
traits - extend primitive
*/

// declare trait - common behaviour interface
trait Some {
    fn do_some(&self);
}

// implement behaviour for structs
impl Some for u32 {
    fn do_some(&self) {
        println!("Some do_some {}", self);
    }
}

fn main() {
    let x: u32 = 123;
    x.do_some();
}
