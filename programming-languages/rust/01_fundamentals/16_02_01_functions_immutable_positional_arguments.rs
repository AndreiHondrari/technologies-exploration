/*
Functions - immutable positional arguments
*/

fn do_some(x: u32, y: u32) {
    println!("do_some {} {}", x, y);
}

fn main() {
    do_some(11, 22);
    do_some(33, 44);
}
