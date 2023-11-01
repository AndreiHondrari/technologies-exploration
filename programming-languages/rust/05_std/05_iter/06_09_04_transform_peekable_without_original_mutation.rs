/*
Iterations - Transform - TODO
*/

use std::iter::Peekable;

fn hprint() {
    println!("{}", "-".repeat(50));
}

macro_rules! head_print {
    ($message:expr) => {
        println!("\n{}", $message);
        hprint();
    };
}

fn main() {
    type ValuesIterator = std::vec::IntoIter<u16>;

    let values: Vec<u16> = vec![11, 22, 33, 44, 55, 66, 77, 88, 99];

    let mut values_iterator: ValuesIterator = values.into_iter();

    // move the iterator a bit further
    println!("next {:?}", values_iterator.next().unwrap());
    println!("next {:?}", values_iterator.next().unwrap());

    // clone the iterator
    let values_iterator_copy: ValuesIterator = values_iterator.clone();

    // peek
    head_print!("new peeker");

    let mut peek_iterator: Peekable<ValuesIterator> = values_iterator_copy.peekable();
    println!("peek A: {:?}", peek_iterator.peek());
    println!("peek A: {:?}", peek_iterator.peek());
    println!("peekable next A: {:?}", peek_iterator.next());
    println!("peek A: {:?}", peek_iterator.peek());

    head_print!("back to original");
    // IT WORKS because peekable() absorbed a clone
    // NOTICE the value is advanced further because of peekable control
    println!("next {:?}", values_iterator.next().unwrap());
}
