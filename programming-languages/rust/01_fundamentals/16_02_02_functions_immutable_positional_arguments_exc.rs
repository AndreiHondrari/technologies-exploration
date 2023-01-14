/*
Functions - immutable positional arguments - can not change exception
*/

fn do_some(x: u32) {
    println!("A {}", x);
    x = 999;  // will throw error
    println!("B {}", x);
}

fn main() {
    do_some(11);
}
