/*
Arrays - copy slice to vector
*/

fn main() {
    let collection: &[u8] = &[11, 22, 33, 44];

    let other: Vec<u8> = collection.to_vec();

    for x in other {
        println!("{x}");
    }
}
