/*
Control flow - explicit boolean conditions

Rust compiler will not convert numeric variables to booleean values,
hence the conditions must be explicit
*/


fn main() {

    let x = 10;

    if x > 0 {
        println!("Yay");
    }

    if x {  // -> Will throw error
        println!("Ahoy!");
    }
}
