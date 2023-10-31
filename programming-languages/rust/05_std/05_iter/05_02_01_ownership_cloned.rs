/*
Ownership - Cloned
*/

use std::iter::Cloned;
use std::slice::Iter;

fn main() {
    let values: Vec<u16> = vec![11, 22, 33];

    let values_iterator: Iter<'_, u16> = values.iter();
    let mut values_cloned_iterator: Cloned<Iter<'_, u16>> = values_iterator.cloned();

    let x: u16 = values_cloned_iterator.next().unwrap();
    println!("{x}");

    let k: u16 = values[0];
    println!("{k}");
}
