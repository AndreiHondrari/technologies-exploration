/*
Ownership and copy of immutable data to mutable data

*/

fn main() {
    let x: i32 = 1234;
    let mut y: i32 = x;  // x is copied into a new place called y

    println!("BEF {}, {}", x, y);  // both are usable here distinctively

    y = 7777;  // only y is changed in memory

    println!("AFT {}, {}", x, y);  // both are usable here distinctively
}
