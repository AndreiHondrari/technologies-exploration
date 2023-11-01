/*
Iterations - Transform - filter but copied
*/

use std::iter::{Copied, Filter};
use std::slice::Iter;

fn main() {
    let values: Vec<u16> = (1..20).into_iter().collect();

    /*
    Notice the signature of the filter predicate.

    Compared to the regular iter(), the values are copied into the iterator,
    and the predicate gets the reference of those copies.
    */
    let filtered_values_iterator: Filter<Copied<Iter<'_, u16>>, fn(&u16) -> bool> =
        values.iter().copied().filter(|x: &u16| *x % 2 == 0);

    let result: Vec<_> = filtered_values_iterator.collect();

    println!("{result:?}");
}
