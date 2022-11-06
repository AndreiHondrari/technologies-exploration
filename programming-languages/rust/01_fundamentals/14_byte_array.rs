/*
Byte array
*/

fn main() {
    let arr1: &[u8; 4] = b"\x61\x62\x63\x64";  // declare byte array

    for x in arr1 {
        print!("{} ", x);
    }
    println!();
}
