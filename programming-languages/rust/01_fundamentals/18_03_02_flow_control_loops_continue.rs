/*
Control flow - loops skipping iterations

Loop while skipping some iterations
*/


fn main() {

    let mut i = 0;

    loop {
        i += 1;

        if i >= 10 { break }; // interrupt loop at the end

        if i % 2 == 0 { continue };  // skip iteration based on condition

        println!("value {i}");  // use value
    }
}
