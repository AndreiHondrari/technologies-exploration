/*
Iterations - Transform - filter
*/

use std::iter::Filter;
use std::slice::Iter;

fn main() {
    let values: Vec<u16> = (1..20).into_iter().collect();

    /*
    Notice the signature of the filter predicate.

    it is a double reference and the reason are:
        - a reference comes from the original iterator
        - a reference is applied by the Filter iterator

    Alternative ways to make this lambda beautiful would be

        Destructure the reference once and dereference it in the evaluator
        |&x: &u6| *x + ...

        Destructure the reference once and let automatic dereferencing work
        |&x: &u6| x + ...

    Another way would be to use alternative kinds of iterators:
        IntoIterator, Cloned, Copied
    */
    let filtered_values_iterator: Filter<Iter<'_, u16>, fn(&&u16) -> bool> =
        values.iter().filter(|x: &&u16| **x % 2 == 0);

    let result: Vec<_> = filtered_values_iterator.collect();

    println!("{result:?}");
}
