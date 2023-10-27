/*
Arrays - copy slice to vector - change original after copy

The copy vector is not affected by changes in the original slice.
*/

fn main() {
    let collection: &mut [u8] = &mut [11, 22, 33, 44];

    let other: Vec<u8> = collection.to_vec();

    println!("OTHER BEFORE");
    println!("{}", "-".repeat(50));
    for x in other.iter() {
        println!("{x}");
    }

    println!("\n--> change collection\n");
    collection[1] = 77;
    collection[2] = 88;

    println!("OTHER AFTER");
    println!("{}", "-".repeat(50));
    for x in other.iter() {
        println!("{x}");
    }
}
