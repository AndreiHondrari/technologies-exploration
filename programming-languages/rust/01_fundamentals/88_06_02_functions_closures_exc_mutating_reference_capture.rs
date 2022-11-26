/*
Functions - Closures

Closures by default borrow variables from outside their scope as a reference
*/


fn main() {

    let mut x = 123;
    let mut _y = x;  // to silence the compiler

    let my_func = || { println!("my_func {}", x); };  // borrows x as reference

    x = 333;  // throws error because f1 borrows x as a reference and uses it later
    my_func();  // uses the reference of x

    _y = x;  // to silence the compiler
}
