use std::fs::*;
use std::io::Read;

fn main() {
    let mut some_file = File::open("some.txt").unwrap();
    let mut content = String::new();
    some_file.read_to_string(&mut content).ok();

    let content = content; // freeze string

    let lines = content.trim().split('\n');

    for (i, line) in lines.enumerate() {
        println!("[{i:2}]\t {line}");
    }
}
