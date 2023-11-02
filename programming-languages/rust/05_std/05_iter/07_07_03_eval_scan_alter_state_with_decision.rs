/*
Iterations - Evaluation - Scan - Alter state
*/

use std::iter::Scan;

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u64>;

    let section_1 = (1..5 + 1).into_iter();
    let section_2 = section_1.clone().rev();

    let values: Vec<u64> = section_1.chain(section_2).collect();

    let values_iterator: ValuesIterator = values.iter();

    /*
    Notice that state IS MUTATED between iterations.
    Make decisions based on the collection variable.
    */
    let scanned_values: Scan<ValuesIterator, u64, fn(&mut u64, &u64) -> Option<u64>> =
        values_iterator.scan(1, |state: &mut u64, &current_value: &u64| {
            // alter iterator state on each iteration based on collection variable
            *state = if current_value >= 4 { 1_000 } else { 1 };

            // combine the altered state with the element from the collection
            Some(*state * current_value)
        });

    for x in scanned_values {
        println!("{:?}", x);
    }
}
