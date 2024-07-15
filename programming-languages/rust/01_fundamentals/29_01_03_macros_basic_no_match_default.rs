/*
Macros - no match - NO COMPILATION
*/

macro_rules! some_thing {
    (111) => {
        println!("MATCHED");
    };

    // tt = Token Tree - an Abstract Syntax Tree (AST) concept
    ($other:tt) => {
        // catches everything else
        println!("HO NO :(");
    };
}

fn main() {
    some_thing!(222);
}
