/*
Functions - Closures

Closures capture only variables that are not defined inside
*/


fn main() {

    let mut x = 123;
    let mut _y = x;  // to silence the compiler

    // don't capture anything
    let my_func = || {
        let x = 777;  // define an internal x
        println!("my_func {}", x);  // use the internal x
    };

    my_func();  // uses the value defined insidex

    x = 333;  // mutates outside x

    my_func();  // uses the value defined inside

    _y = x;  // to silence the compiler
}