/*
Iterations - Transform - Zip
*/

use std::iter::Zip;
use std::slice::Iter;

fn main() {
    // NOTICE that 44 does not have a pair so it is not listed in the result
    let v1: Vec<u16> = vec![11, 22, 33, 44];
    let v2: Vec<u16> = vec![999, 777, 555];

    let v1_iterator: Iter<'_, u16> = v1.iter();
    let v2_iterator: Iter<'_, u16> = v2.iter();

    let zip_iterator: Zip<Iter<'_, u16>, Iter<'_, u16>> = v1_iterator.zip(v2_iterator);

    let result: Vec<(&u16, &u16)> = zip_iterator.collect();

    println!("{:?}", result);
}
