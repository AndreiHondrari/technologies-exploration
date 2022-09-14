

fn main() {

    println!("Fixed declared array");
    let arr1: [i32; 2] = [0; 2];
    for x in arr1 {
        println!("{x}");
    }

    println!("\nDynamically declared array");
    let arr2 = [1, 2, 3];
    for x in arr2 {
        println!("{x}");
    }
}
