/*
Ownership - Copied - Values are copied into the iterator
*/

use std::iter::Copied;
use std::slice::Iter;

fn main() {
    let values: Vec<u16> = vec![11, 22, 33];
    let values_iterator: Iter<'_, u16> = values.iter();
    let mut values_copied_iterator: Copied<Iter<'_, u16>> = values_iterator.copied();

    let x: u16 = values_copied_iterator.next().unwrap();
    println!("from iterator:    {x}");

    let k: u16 = values[0];
    println!("from vector:      {k}");
}
