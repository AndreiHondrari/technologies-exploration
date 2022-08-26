

fn main() {
    // immutable variable
    let x = 11;

    // mutable variable
    let mut y = 77;

    // lines necessary otherwise
    // compiler complains
    println!("y before: {y}")
    y = 22;

    // constant: notice type anotation is mandatory
    const Z: i32 = 33;

    println!("{x}, {y}, {Z}");
}
