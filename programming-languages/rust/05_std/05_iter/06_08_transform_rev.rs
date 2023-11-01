/*
Iterations - Transform - Reverse
*/

use std::iter::Rev;
use std::slice::Iter;

fn main() {
    let values: Vec<u16> = (1..10 + 1).into_iter().collect();

    let rev_iterator: Rev<Iter<'_, u16>> = values.iter().rev();

    let result: Vec<_> = rev_iterator.collect();

    println!("{result:?}");
}
