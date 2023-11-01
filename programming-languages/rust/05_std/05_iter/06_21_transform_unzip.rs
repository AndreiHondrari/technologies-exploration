/*
Iterations - Transform - Unzip
*/

use std::iter::Copied;

fn main() {
    type Kek = (u16, u16);
    type ValuesIterator<'a> = std::slice::Iter<'a, Kek>;
    let zipped_values: Vec<(u16, u16)> = vec![(11, 555), (22, 777), (33, 999)];

    println!("zipped:   {:?}", zipped_values);

    // NOTICE it needs a cloned() or copied() because unzip can't handle &(u16, u16)
    let values_iterator: Copied<ValuesIterator> = zipped_values.iter().copied();

    // unzip::<u16, u16, Vec<u16>, Vec<u16>> => (A, B, FromA, FromB) -> (FromA, FromB)
    let (v1, v2): (Vec<u16>, Vec<u16>) = values_iterator.unzip();

    println!("v1:       {:?}", v1);
    println!("v2:       {:?}", v2);
}
