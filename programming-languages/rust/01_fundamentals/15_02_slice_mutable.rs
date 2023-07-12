/*
Slice - mutable slice

Altering an value at an index in the slice, is relative to the original vector.
*/

fn main() {
    let mut arr1: [i32; 10] = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100];
    let arr1ref: &mut [i32] = &mut arr1[2..6];

    arr1ref[0] = 777;
    arr1ref[3] = 999;

    for item in arr1.iter().enumerate() {
        let value_pack: &(usize, &i32) = &item;
        println!("{:?}", value_pack);
    }
}
