/*
Macros - basic - exact value
*/

macro_rules! some_thing {
    (111) => {
        println!("MATCHED");
    };

    (banana) => {
        // notice you can use labels
        println!("BANANA");
    };
}

fn main() {
    some_thing!(111);
    some_thing!(banana);
}
