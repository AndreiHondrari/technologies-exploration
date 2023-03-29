/*
smart pointers - heap
*/

fn main() {
    // allocate value on heap
    let x: Box<u16> = Box::new(123);

    // extract value from smart pointer
    let p: u16 = *x;

    println!("{}", p);
}
