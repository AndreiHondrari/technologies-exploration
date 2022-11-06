/*
Various literals
*/

fn main() {
    let v1: u32 = 12_345;
    let v2: u8 = 0xff; // 255
    let v3: u8 = 0o377; // 255
    let v4: u8 = 0b1111_1111; // 255
    let v5: u8 = b'\xff'; // 255
    let v6: char = '\x41';

    println!("{}", v1);
    println!("{}", v2);
    println!("{}", v3);
    println!("{}", v4);
    println!("{}", v5);
    println!("{}", v6);
}
