/*
Macros - no match - NO COMPILATION
*/

macro_rules! some_thing {
    (111) => {
        println!("MATCHED");
    };
}

fn main() {
    some_thing!(222); // WILL NOT COMPILE
}
