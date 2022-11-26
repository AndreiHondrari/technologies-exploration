/*
Functions - Closures

Closures can capture variables from outside by value by using the keyword 'move'
*/


fn main() {

    let mut x = 123;
    let mut _y = x;  // to silence the compiler

    // capture x as a standalone isolated variable
    let my_func = move || { println!("my_func {}", x); };

    my_func();  // uses the value copied from x

    x = 333;  // mutates outside x

    my_func();  // uses the value copied from x

    _y = x;  // to silence the compiler
}
