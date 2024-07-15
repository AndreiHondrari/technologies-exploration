/*
Destructure var tuples as refereces
*/

fn main() {
    let a = 123u16;
    let b = 3.14f32;

    println!("{a} {b}");

    // structure as tuple (notice a and b are copied into the tuple)
    let tup: (u16, f32) = (a, b);

    /*
    destructure from tuple as references.

    x is &u16
    y is &f32

    because destructuring from a reference
    causes the destructured parts to be
    interpolated as references.
    */
    let (x, y): &(u16, f32) = &tup;

    println!("{x} {y}");
}
