/*
Slices

Slices of arr[a..b] form always return [T]
which is a sort of "fat pointer" (dynamically sized type)
that has the address of the first element in the slice
and the length of the slice.

Normally you can't use this [T] slice directly,
but must use the reference operator on it,
to be able to use both the pointer and the length
of the memory structure.

(if you ask me, it's mostly a conventional thing
to make memory handling explicit)
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
