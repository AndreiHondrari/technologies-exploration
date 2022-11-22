/*
Functions - Closures

Closures are basically anonymous functions.
*/


fn main() {
    let my_func: fn() = || { println!("calling closure")};
    my_func();

}
