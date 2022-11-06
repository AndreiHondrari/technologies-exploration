/*
Primitive string
*/

fn main() {
    //
    let msg1: &str = "This is msg1";
    let msg2: &'static str = "This is the msg2";

    println!("{}", msg1);
    println!("msg1 length: {}", msg1.len());

    println!("{}", msg2);
    println!("msg2 length: {}", msg2.len());
}
