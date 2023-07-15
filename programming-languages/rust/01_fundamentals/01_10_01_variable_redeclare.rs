/*
Redeclare variable

A variable can be redeclared from mutable to immutable and bac
as many times as we'd like
*/

fn main() {
    // initial declaration
    let mut x = 11;
    println!("A 0 | {x}");

    // a mutation
    x = 22;
    println!("A 1 | {x}");

    // FREEZE
    let x = x;
    println!("B   | {x}");

    // can no longer mutate it here
    // x = 33; // WILL NOT WORK

    let mut x = x;

    println!("C 0 | {x}");

    x = 44;

    println!("C 1 | {x}");
}
