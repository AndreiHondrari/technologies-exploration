/*
String
*/


fn main() {
    let mut msg = String::from("Hello");
    println!("BEFORE {msg}");

    msg.push(',');
    msg.push_str(" world!");

    println!("AFTER  {msg}");
}
