/*
Iterations - Transform - Take While
*/

use std::iter::TakeWhile;

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u16>;

    let values: Vec<u16> = (10..1_000 + 1).step_by(10).collect();

    let values_iterator: ValuesIterator = values.iter();

    let take_iterator: TakeWhile<ValuesIterator, fn(&&u16) -> bool> =
        values_iterator.take_while(|&x: &&u16| *x < 200);

    let result: Vec<&u16> = take_iterator.collect();

    println!("{:?}", result);
}
