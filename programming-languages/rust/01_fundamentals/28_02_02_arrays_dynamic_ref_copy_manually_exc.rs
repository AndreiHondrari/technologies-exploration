/*
Arrays - copy array slice to a new array - [type; usize] expects a constant
DOES NOT COMPILE
*/

fn main() {
    let collection: &[u8] = &[11, 22, 33, 44];

    let collection_size: usize = collection.len();

    // WILL NOT WORK - collection_size is not constant
    let mut other: [u8; collection_size] = [0; collection_size];

    for i in 0..collection_size {
        let x: u8 = collection[i];
        println!("{x}");
        other[i] = x;
    }
}
