/*
Fixed and dynamically declared arrays.

The fixed declared array will initialize
all slots with the given default value.
The actual values need to be specified
later for each slot.

The dynamically declared array will
need the exact values as part of the
declaration.
*/

fn main() {

    println!("Fixed declared array");
    let arr1: [i32; 2] = [123; 2];
    for x in arr1 {
        println!("{x}");
    }

    println!("\nDynamically declared array");
    let arr2 = [1, 2, 3];
    for x in arr2 {
        println!("{x}");
    }
}
