/*
Arrays - copy array slice to a new array - [type; usize] expects a constant
*/

fn main() {
    const COLLECTION: &[u8] = &[11, 22, 33, 44];

    const COLLECTION_SIZE: usize = COLLECTION.len();

    let mut other: [u8; COLLECTION_SIZE] = [0; COLLECTION_SIZE];

    for i in 0..COLLECTION_SIZE {
        let x: u8 = COLLECTION[i];
        println!("{i}: {x}");
        other[i] = x;
    }
}
