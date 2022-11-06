/*
Primitive string

Escapes and as raw.
*/

fn main() {
    let msg1: &str = "\x61\x62\x63\x64";
    let msg2: &str = r"\x61\x62\x63\x64";  // does not escape

    println!("{}", msg1);
    println!("{}", msg2);
}
