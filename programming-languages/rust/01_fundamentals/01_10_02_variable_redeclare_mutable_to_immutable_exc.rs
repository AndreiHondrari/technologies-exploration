/*
Redeclare variable as immutable (from mutable) - DOES NOT COMPILE
*/

fn main() {
    // initial declaration
    let mut x = 11;
    println!("A | {x}");

    // a mutation
    x = 22;
    println!("A | {x}");

    // FREEZE
    let x = x;
    println!("{x}");

    // can no longer mutate it here
    x = 33; // WILL NOT WORK
}
