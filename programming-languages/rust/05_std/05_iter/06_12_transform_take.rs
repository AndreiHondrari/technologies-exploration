/*
Iterations - Transform - Take
*/

use std::iter::Take;

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u16>;

    let values: Vec<u16> = (10..1_000 + 1).step_by(10).collect();

    let values_iterator: ValuesIterator = values.iter();

    let take_iterator: Take<ValuesIterator> = values_iterator.take(15);

    let result: Vec<&u16> = take_iterator.collect();

    println!("{:?}", result);
}
