/*
Slices
*/

fn main() {
    let arr1 = [11, 22, 33, 44, 55, 66, 77, 88, 99];

    println!("2 -> 6 slice");
    let arr1_slice: &[i32] = &arr1[2..6];
    for x in arr1_slice {
        println!("{}", x);
    }

    println!("\n_ -> 4 slice");
    let arr2_slice: &[i32] = &arr1[..4];
    for x in arr2_slice {
        println!("{}", x);
    }

    println!("\n4 -> _ slice");
    let arr3_slice: &[i32] = &arr1[4..];
    for x in arr3_slice {
        println!("{}", x);
    }
}
