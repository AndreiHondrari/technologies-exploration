/*
Arrays - deref array slice - DOES NOT COMPILE
*/

fn main() {
    let collection: &[u8] = &[11, 22, 33, 44];

    let other = *collection; // WILL NOT COMPILE (the deref part) - no size known

    for x in collection {
        println!("{x}");
    }
}
