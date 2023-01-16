/*
Control flow - loops - break return from function

Loops can be used as return values for functions
*/

fn my_func() -> u16 {
    loop {
        break 1234;
    }
}

fn main() {
    let x = my_func();
    println!("{x}");
}
