/*
Control flow - loops - iterate over collection

Collections can be iterated over in three distinct ways using flow control.
*/


fn iterate_with_loops(arr: [i32; 3]) {
    let mut i = 0;
    loop {
        if i >= 3 {break};
        println!("V1 {}", arr[i]);
        i += 1;
    }
}

fn iterate_with_while(arr: [i32; 3]) {
    let mut i = 0;
    while i < arr.len() {
        println!("V2 {}", arr[i]);
        i += 1;
    }
}

fn iterate_with_for(arr: [i32; 3]) {
    for i in 0..arr.len() {
        println!("V3 {}", arr[i]);
    }

    println!();

    for x in arr {
        println!("V4 {}", x);
    }
}


fn main() {

    let arr: [i32; 3] = [1, 2, 3];

    iterate_with_loops(arr);
    println!();

    iterate_with_while(arr);
    println!();

    iterate_with_for(arr);
    println!();


    println!("Done");
}
