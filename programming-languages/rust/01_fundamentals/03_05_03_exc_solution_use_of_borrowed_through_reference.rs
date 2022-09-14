

fn main() {
    // define a mutable variable
    let mut x = 123;

    // open a scope
    {
        // borrow variable as a mutable reference
        let x_ref = &mut x;

        // use reference
        let v2 = x_ref;
        println!("{}", v2);
    }

    let v1 = x;
    println!("{}", v1);
}
