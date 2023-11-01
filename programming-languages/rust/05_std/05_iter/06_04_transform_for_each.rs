/*
Iterations - Transform - For Each
*/

fn do_something(x: &u8) {
    println!("something: {}", *x);
}

fn main() {
    let values: Vec<u8> = (0..5).into_iter().collect();

    values.iter().for_each(&do_something);
}
