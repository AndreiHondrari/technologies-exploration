/*
Explicit warning when changing before using.

It might be that you intended to
declare an immutable.
*/


fn main() {
    let mut x = 11;
    // not used here
    x = 22;
    println!("{x}")
}
