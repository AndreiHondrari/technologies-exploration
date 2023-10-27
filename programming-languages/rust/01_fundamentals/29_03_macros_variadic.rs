/*
Macros - variadic
*/

macro_rules! some_thing {
    ($( $kek:expr ), *) => {
        $(
            println!("{}", $kek);
        )*  // for each item layout this code
    };
}

fn main() {
    some_thing!(11, 22, 33);
}
