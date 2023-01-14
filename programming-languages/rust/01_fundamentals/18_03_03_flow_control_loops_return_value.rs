/*
Control flow - loops - return values

Use a value returned by a loop
*/


fn main() {

    let mut i = 0;

    let result = loop {
        if i >= 10 { break 111 };
        i += 1;
    };

    println!("Result {result}");
}
