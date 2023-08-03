/*
Polymorphism - Parametric
*/

use std::ops::Add;

fn do_some<T>(x: T) -> T
where
    // Copy necessary so that when adding
    // the compiler will not assume
    // that we are moving the first x in the expression
    T: Copy + Add<Output = T>,
{
    return x + x;
}

fn main() {
    let result = do_some(11);
    println!("{result}");
}
