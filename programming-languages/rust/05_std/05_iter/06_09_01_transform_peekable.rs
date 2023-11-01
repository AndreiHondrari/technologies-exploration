/*
Iterations - Transform - TODO
*/

use std::iter::Peekable;

fn main() {
    type ValuesIterator = std::vec::IntoIter<u16>;

    let values: Vec<u16> = vec![11, 22, 33, 44, 55, 66, 77, 88, 99];

    let mut values_iterator: ValuesIterator = values.into_iter();

    // move the iterator a bit further
    println!("next {:?}", values_iterator.next().unwrap());
    println!("next {:?}", values_iterator.next().unwrap());

    // peek
    let mut peek_iterator: Peekable<ValuesIterator> = values_iterator.peekable();
    let maybe_value: Option<&u16> = peek_iterator.peek();

    match maybe_value {
        Some(value) => {
            println!("peeked value: {:?}", value);
        }

        None => {
            println!("peeked nothing");
        }
    }

    // WON'T WORK ! the values iterator is moved into the peekable iterator
    // println!("next {:?}", values_iterator.next().unwrap());
}
