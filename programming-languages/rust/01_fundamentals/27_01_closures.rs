/*
Functions - Closures

Closures are basically anonymous functions.
Compared to functions, they can use the outside scope.
*/

fn main() {
    let my_func: fn() = || println!("calling closure");
    my_func();
}
