/*
Iterators - skip with nth()
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
    let mut values_iterator = values.iter();

    let result = values_iterator.nth(3);
    println!("advance by 3      result {:?}", result);

    let result = values_iterator.next();
    println!("next              {:?}", result);

    let result = values_iterator.nth(100);
    println!("advance by 100    result {:?}", result);
}
