/*
Control flow - loops - breaking outer loop by label and return

You can get a value from a labeled loop
*/


fn main() {
    let x = 'out_loop: loop {
        loop {
            break 'out_loop 123;
        }
    };

    println!("{x}");
}
