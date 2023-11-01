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

    // get ref
    let ref_values_iterator: &mut ValuesIterator = values_iterator.by_ref();

    // peek
    head_print!("new peeker A");

    let mut peek_iterator: Peekable<&mut ValuesIterator> = ref_values_iterator.peekable();
    println!("peek A: {:?}", peek_iterator.peek());
    println!("peek A: {:?}", peek_iterator.peek());
    println!("peekable next A: {:?}", peek_iterator.next());
    println!("peek A: {:?}", peek_iterator.peek());

    head_print!("new peeker B");

    let mut peek_iterator: Peekable<&mut ValuesIterator> = ref_values_iterator.peekable();
    println!("peek B: {:?}", peek_iterator.peek());
    println!("peek B: {:?}", peek_iterator.peek());

    head_print!("back to original");
    // IT WORKS because peekable() absorbed only a ref
    // NOTICE the value is advanced further because of peekable control
    println!("next {:?}", values_iterator.next().unwrap());
}
