/*
Ownership - Into Iter vs Cloned - Demonstrate into iter move

DOES NOT COMPILE !
*/

use std::iter::IntoIterator;

fn main() {
    let values: Vec<u16> = vec![11, 22, 33];

    let mut iterator: std::vec::IntoIter<u16> = IntoIterator::into_iter(values);

    let x: u16 = iterator.next().unwrap();
    println!("from iterator:    {x}");

    /*
    The `values[0]` borrow is the reason why it does not compile.
    into_iter() moves the elements into the iterator.
    */
    let k: u16 = values[0];
    println!("from vector:      {k}");
}
