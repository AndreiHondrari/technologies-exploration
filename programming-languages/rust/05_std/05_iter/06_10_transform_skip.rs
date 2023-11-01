/*
Iterations - Transform - skip
*/

use std::iter::Skip;

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u16>;

    let values: Vec<u16> = vec![11, 22, 33, 44, 55, 66, 77, 88, 99];

    let values_iterator: ValuesIterator = values.iter();

    let mut skip_values_iterator: Skip<ValuesIterator> = values_iterator.skip(3);
    println!("skip by 3");

    let result = skip_values_iterator.next();
    println!("next {:?}", result);

    let mut skip_values_iterator = skip_values_iterator.skip(100);
    println!("skip by 100");

    let result = skip_values_iterator.next();
    println!("next {:?}", result);
}
