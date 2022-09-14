

fn main() {
    // define a mutable variable
    let mut x = 123;

    // borrow variable as a mutable reference
    let x_ref = &mut x;

    // will not work
    // because it was borrowed
    let v1 = x;

    let v2 = x_ref;

    println!("{}", v1);
    println!("{}", v2);
}
