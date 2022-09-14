

fn main() {
    // define original variables
    let x = 11;
    let mut y = 22;

    // reference to immutable variable
    let x_ref = &x;
    println!("x_ref {}", x_ref);

    // reference to mutable variable
    {
        let y_ref = &mut y;
        *y_ref = 33;
        println!("y_ref {}", y_ref);
    }

    let y_ref2 = &mut y;

    println!("y     {}", y);
    println!("y     {}", y_ref2);
}
