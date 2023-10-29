/*
Iterators - laziness
*/

use std::iter::Map;
use std::slice::Iter;

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
    let values: [u8; 3] = [11, 22, 33];
    println!("original array:    {:?}", values);

    head_print!("Demonstrate laziness of iterators");
    let values_iterator = values.iter();

    let mut values_iterator: Map<Iter<'_, u8>, fn(&u8) -> ()> =
        values_iterator.map(|x| println!("step {}", x));

    println!("foo");
    values_iterator.next();
    println!();

    println!("bar");
    values_iterator.next();
    println!();

    println!("kek");
    values_iterator.next();
    println!();
}
