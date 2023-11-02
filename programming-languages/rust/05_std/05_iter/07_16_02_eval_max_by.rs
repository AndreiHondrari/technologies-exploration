/*
Iterations - Evaluation - Max By
*/

use std::cmp::Ordering;

fn main() {
    let values: Vec<u16> = vec![1, 2, 3, 55, 111, 222, 333];

    // by A
    let result = values.iter().max_by(|&a: &&u16, &_b: &&u16| {
        // for demonstration purposes we force Greater for 55
        if *a == 55 {
            Ordering::Greater
        } else {
            Ordering::Less
        }
    });
    println!("by a -> {:?}", result);

    // by B
    let result = values.iter().max_by(|&_a: &&u16, &b: &&u16| {
        // for demonstration purposes we force Less for 55
        if *b == 55 {
            Ordering::Less
        } else {
            Ordering::Greater
        }
    });
    println!("by b -> {:?}", result);
}
