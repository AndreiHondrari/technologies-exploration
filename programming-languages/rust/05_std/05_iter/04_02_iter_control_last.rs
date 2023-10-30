/*
Iterations - Control - last
*/

use std::slice::Iter;

fn main() {
    let values: Vec<u16> = vec![11, 22, 33, 44];

    let values_iterator: Iter<'_, u16> = values.iter();

    let result = values_iterator.last();

    match result {
        Some(value) => {
            println!("last value: {}", value)
        }

        None => {
            println!("No value");
        }
    }
}
