/*
Explicit error when changing immutables.
*/

fn main() {
    let x = 11;
    x = 22;
    println!("{x}");
}
