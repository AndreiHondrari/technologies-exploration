use std::fs::*;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut some_file: File = File::create("test-file.txt")?;
    let content = String::from("a b c d e f g h");
    some_file.write(&content.as_bytes())?;

    Ok(())
}
