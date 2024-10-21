/*
Slices - COMPILER ERROR

Mutating an array that is borrowed via a slice, is illegal.
*/

fn main() {
    let mut arr1 = [11, 22, 33, 44, 55, 66, 77, 88, 99];

    println!("2 -> 6 slice");
    let slice: &[i32] = &arr1[2..6];

    arr1[3] = 9999; // WILL NOT WORK -> mutating borrowed memory (via slice)

    for x in slice {
        println!("{}", x);
    }

    arr1[3] = 1234; // just to avoid warning from compiler
}
