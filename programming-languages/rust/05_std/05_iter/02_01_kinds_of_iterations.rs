/*
Iterators - kinds of iterations
*/

use std::slice::{Iter, IterMut};

macro_rules! head_print {
    ($message:expr) => {
        println!("\n{}", $message);
        println!("{}", "-".repeat(50));
    };
}

/*
iteration over references.
next() gives references
*/
fn iterator_on_references(values: [u8; 3]) {
    let mut values_iterator: Iter<'_, u8> = values.iter();
    let val: &u8 = values_iterator.next().unwrap();
    println!("value {}", val);
}

/*
iteration over mutable references.
next() gives mutable references
*/
fn iterator_on_mutable_references(mut values: [u8; 3]) {
    println!("array before mutation:    {:?}", values);

    println!("mutate second value ...");
    let mut values_iterator: IterMut<'_, u8> = values.iter_mut();
    values_iterator.next(); // go to middle value
    let val: &mut u8 = values_iterator.next().unwrap();
    *val = 99;

    println!("array after mutation:     {:?}", values);
}

/*
iteration over values.
next() gives values

Please notice that in some cases the values are moved from the original array into the iterator.
This means you can no longer use those values from the original array/collection.
*/
fn iterator_on_values(values: [u8; 3]) {
    /*
    `values.into_iter()` works normally for fixed size arrays only in edition 2021
    because of
    https://doc.rust-lang.org/edition-guide/rust-2021/IntoIterator-for-arrays.html
    */
    let mut values_iterator: std::array::IntoIter<u8, 3> = IntoIterator::into_iter(values);
    let val: u8 = values_iterator.next().unwrap();
    println!("value {}", val);
}

fn main() {
    let values: [u8; 3] = [11, 22, 33];
    println!("original array:    {:?}", values);

    head_print!("Iterator on references");
    iterator_on_references(values);

    head_print!("Iterator on mutable references");
    iterator_on_mutable_references(values);

    head_print!("Iterator on values");
    iterator_on_values(values);
}
