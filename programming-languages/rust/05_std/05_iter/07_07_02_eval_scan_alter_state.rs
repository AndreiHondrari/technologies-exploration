/*
Iterations - Evaluation - Scan - Alter state
*/

use std::iter::Scan;

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u64>;

    let values: Vec<u64> = (1..9 + 1).into_iter().collect();

    let values_iterator: ValuesIterator = values.iter();

    /*
    Notice that state IS MUTATED between iterations.

    This is useful when you want to alter some term/factor on a
    different trajectory that the collection variable.

    Can also make decisions based on the collection variable
    */
    let scanned_values: Scan<ValuesIterator, u64, fn(&mut u64, &u64) -> Option<u64>> =
        values_iterator.scan(10, |state: &mut u64, &current_value: &u64| {
            // alter iterator state on each iteration
            *state *= 10;

            // combine the altered state with the element from the collection
            Some(*state * current_value)
        });

    for x in scanned_values {
        println!("{:?}", x);
    }
}
