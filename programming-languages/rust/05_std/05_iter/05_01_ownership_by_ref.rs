/*
Ownership - By Ref

When using transformation methods like Take, Skip or StepBy,
the ownership on the iterator is lost to those new iterators.

In order to keep ownership we need to pass a reference to the
iterator.

PLEASE NOTICE the iterator is altered through the reference.
*/

use std::iter::Take;
use std::slice::Iter;

fn main() {
    let values: Vec<u16> = vec![11, 22, 33, 44, 55, 66, 77];

    let mut values_iterator: Iter<'_, u16> = values.iter();

    // Notice that we obtain a reference to an iterator
    let values_iterator_reference: &mut Iter<'_, u16> = values_iterator.by_ref();

    /*
    Notice that the resulting take iterator has ownership of the reference to the iterator
    and not to the iterator itself.
    */
    let mut values_take: Take<&mut Iter<'_, u16>> = values_iterator_reference.take(2);
    println!("took              {}", values_take.next().unwrap());
    println!("took              {}", values_take.next().unwrap());

    // we can continue using the original iterator (altered through the reference
    println!("original next     {}", values_iterator.next().unwrap());
    println!("original next     {}", values_iterator.next().unwrap());
}
