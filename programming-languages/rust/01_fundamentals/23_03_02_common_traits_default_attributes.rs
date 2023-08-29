/*
common traits - default - on specific attribute
*/

use std::default::*;

#[allow(dead_code)]
#[derive(Debug)]
struct Some {
    x: u16,
    y: i32,
}

fn main() {
    let s1: Some = Some {
        x: 777,
        y: Default::default(), // the default for i32
    };
    println!("{:?}", s1);
}
