use std::ops::Range;

fn main() {
    let some_range: Range<u8> = 0..10;

    println!("{:?}", some_range.into_iter().collect::<Vec<u8>>());
}
