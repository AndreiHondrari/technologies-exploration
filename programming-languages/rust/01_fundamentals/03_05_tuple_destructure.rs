/*
Destructure var tuples
*/

fn main() {
    let a = 123u16;
    let b = 3.14f32;

    println!("{a} {b}");

    // structure as tuple
    let tup: (u16, f32) = (a, b);

    // destructure from tuple
    let (x, y): (u16, f32) = tup;

    println!("{x} {y} {a} {b}");
}
