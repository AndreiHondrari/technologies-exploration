/*
Iterations - Transform - Enumerator
*/

use std::iter::Enumerate;

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u16>;

    let values: Vec<u16> = (10..1_00 + 1).step_by(10).collect();

    let values_iterator: ValuesIterator = values.iter();

    let enumerator: Enumerate<ValuesIterator> = values_iterator.enumerate();

    let result: Vec<(usize, &u16)> = enumerator.collect();

    for x in result {
        println!("{:?}", x);
    }
}
