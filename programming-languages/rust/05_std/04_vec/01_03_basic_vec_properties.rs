/*
Vectors - properties
*/

fn main() {
    let mut v1: Vec<u16> = vec![];

    // BEFORE
    println!("before");
    println!("{}", "-".repeat(50));

    println!("v1 len    : {}", v1.len());
    println!("v1 empty  : {}", v1.is_empty());
    println!("v1 cap    : {}", v1.capacity());

    // CHANGES
    println!("\ninsert stuff\n");
    v1.push(11);
    v1.push(22);
    v1.push(33);

    // AFTER
    println!("after");
    println!("{}", "-".repeat(50));
    println!("v1 len    : {}", v1.len());
    println!("v1 empty  : {}", v1.is_empty());
    println!("v1 cap    : {}", v1.capacity());
}
