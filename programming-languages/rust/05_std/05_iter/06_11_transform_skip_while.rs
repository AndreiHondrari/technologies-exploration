/*
Iterations - Transform - Skip While
*/

use std::iter::SkipWhile;

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u16>;

    let values: Vec<u16> = vec![1, 5, 4, 7, 20, 15, 200, 160, 500, 420, 1_001];

    let values_iterator: ValuesIterator = values.iter();

    println!("skip until a condition ...");
    let mut skip_values_iterator: SkipWhile<ValuesIterator, fn(&&u16) -> bool> =
        values_iterator.skip_while(|&x: &&u16| *x < 100);

    let result = skip_values_iterator.next();
    println!("next {:?}", result);
}
