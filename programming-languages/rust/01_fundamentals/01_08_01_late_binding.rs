/*
Variable late binding

A variable mutable or immutable can be assigned
at a later time after declaration
*/

fn main() {
    // declare
    let x: i32;
    let mut y: i32;

    // initialize
    x = 11;
    y = 22;

    println!("x {x}");
    println!("y {y}");

    // ignore
    y = 999;
    let _k = y;
}
