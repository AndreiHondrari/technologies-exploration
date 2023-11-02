/*
Iterations - Evaluation - Scan - Unaltered state
*/

use std::iter::Scan;

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u32>;

    let values: Vec<u32> = (1..9 + 1).into_iter().collect();

    let values_iterator: ValuesIterator = values.iter();

    /*
    Notice that state IS NOT mutated between iterations.

    This is useful when you want to apply a variable to a constant.
    */
    let scanned_values: Scan<ValuesIterator, u32, fn(&mut u32, &u32) -> Option<u32>> =
        values_iterator.scan(111, |state: &mut u32, &current_value: &u32| {
            let constant_state: &u32 = state; // freeze state
            Some(*constant_state * current_value)
        });

    for x in scanned_values {
        println!("{:?}", x);
    }
}
