use std::convert::TryInto;
use std::io::*;

fn main() {
    let data: [u8; 9] = [11, 22, 33, 44, 55, 66, 77, 88, 99];
    println!("data:\t {data:?}");

    let mut cursor = Cursor::new(&data);
    cursor.seek(SeekFrom::Current(2)).ok();

    let x = cursor.position();
    println!("pos:\t {x}");

    let mut pos = cursor.position();
    while pos < data.len().try_into().unwrap() {
        let val: u8 = data[pos as usize];
        println!("{pos} -> {val}");

        pos = cursor.seek(SeekFrom::Current(1)).unwrap();
    }
}
