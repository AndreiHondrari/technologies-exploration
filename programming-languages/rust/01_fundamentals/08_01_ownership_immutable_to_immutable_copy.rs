/*
Ownership and copy of immutable data to immutable data

*/

fn main() {
    let x: i32 = 1234;
    let y: i32 = x;  // x is copied into a new place called y
    println!("{}, {}", x, y);  // both are usable here distinctively
}
