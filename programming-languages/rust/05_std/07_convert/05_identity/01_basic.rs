/*
identity function - basic
*/

use std::convert::identity;

fn main() {
    let x = identity(123);
    println!("{}", x);
}
