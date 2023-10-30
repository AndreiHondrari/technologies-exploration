/*
Iterators - skip with skip()
*/

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
    let values: [u8; 9] = [11, 22, 33, 44, 55, 66, 77, 88, 99];
    println!("original array:    {:?}", values);

    head_print!("Demonstrate advance");
    let values_iterator = values.iter();

    let mut values_iterator = values_iterator.skip(3);
    println!("skip by 3");

    let result = values_iterator.next();
    println!("next {:?}", result);

    let _values_iterator = values_iterator.skip(100);
    println!("skip by 100");
}
