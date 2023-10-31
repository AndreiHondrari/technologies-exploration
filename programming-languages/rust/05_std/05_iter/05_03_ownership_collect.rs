/*
Ownership - By Ref
*/

use std::slice::Iter;

fn main() {
    let values: Vec<u16> = vec![11, 22, 33];

    let values_iterator: Iter<'_, u16> = values.iter();
}
