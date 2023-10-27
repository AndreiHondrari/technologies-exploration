/*
Arrays - define dynamic array ref
*/

fn main() {
    let collection: &[u8] = &[11, 22, 33, 44];

    for x in collection {
        println!("{x}");
    }
}
