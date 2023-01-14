/*
Functions - mutable positional arguments
*/

fn do_some(mut x: u32) {
    println!("A {}", x);
    x = 999;
    println!("B {}", x);
}

fn main() {
    do_some(11);
}
