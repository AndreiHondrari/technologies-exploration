use std::ops::Range;

fn main() {
    let some_range: Range<u8> = 0..10;

    let some_range = some_range.rev();

    println!("{:?}", some_range.collect::<Vec<u8>>());
}
