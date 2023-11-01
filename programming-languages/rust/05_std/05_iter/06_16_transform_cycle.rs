/*
Iterations - Transform - Cycle
*/

use std::iter::Cycle;

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u16>;

    let values: Vec<u16> = vec![11, 22, 33];

    let values_iterator: ValuesIterator = values.iter();

    let mut cycle_iterator: Cycle<ValuesIterator> = values_iterator.cycle();

    for _ in 0..20 + 1 {
        print!("{} ", cycle_iterator.next().unwrap());
    }
}
