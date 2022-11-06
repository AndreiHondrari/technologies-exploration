/*
Ownership and copy of mutable data to mutable data

*/

fn main() {
    let mut x: i32 = 1234;
    let mut y: i32 = x;  // x is copied into a new place called y

    x = 3333;

    println!("{}, {}", x, y);  // both are usable here distinctively

    y = 7777;  // only y is changed in memory

    println!("{}, {}", x, y);  // both are usable here distinctively
}
