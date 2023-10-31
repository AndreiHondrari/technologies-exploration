/*
Ownership - Into Iter vs Cloned - Cloned clones the elements into the iterator
*/

use std::iter::Cloned;
use std::slice::Iter;

fn main() {
    let values: Vec<u16> = vec![11, 22, 33];

    let mut iterator: Cloned<Iter<'_, u16>> = values.iter().cloned();

    let x: u16 = iterator.next().unwrap();
    println!("from iterator:    {x}");

    /*
    Still accessible
    */
    let k: u16 = values[0];
    println!("from vector:      {k}");
}
