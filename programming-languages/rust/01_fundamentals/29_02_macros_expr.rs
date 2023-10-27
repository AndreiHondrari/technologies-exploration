/*
Macros - expression
*/

macro_rules! some_thing {
    ($kek:expr) => {
        println!("yolo {}", $kek);
    };
}

fn main() {
    some_thing!(123);
}
