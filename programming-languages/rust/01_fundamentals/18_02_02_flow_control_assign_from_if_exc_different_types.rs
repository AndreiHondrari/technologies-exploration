/*
Control flow - assign from if when using multiple types

Conditional assignment will fails with different types
*/


fn main() {

    let x = 10;

    let v = if x == 10 { 123 } else { "abc" };  // Will throw error

    println!("{}", v);
}
