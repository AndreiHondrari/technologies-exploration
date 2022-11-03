/*
Various ways to print.
*/

// declare some static strings
const MESSAGE_A: &'static str = "aaa";
const MESSAGE_B: &'static str = "bbb";
const MESSAGE_C: &'static str = "ccc";
const MESSAGE_D: &'static str = "ddd";
const MESSAGE_E: &'static str = "eee";
const MESSAGE_F: &'static str = "fff";

fn main() {
    // print directly without newline
    print!("000__");

    // print directly with new line
    println!("111");

    // print a literal as a positional parameter
    println!("{}", "222");

    // print a static string as a positional parameter
    println!("{}", MESSAGE_A);

    // print static string in the inline format
    println!("{MESSAGE_B}");

    // print a composed formatted message
    println!("this {} that", "333");

    // print multiple literals as positional parameters
    println!("{}, {}", "444", "555");

    // print multiple static strings as positional parameters
    println!("{}, {}", MESSAGE_A, MESSAGE_B);

    // print multiple static strings in the inline format
    println!("{MESSAGE_C}, {MESSAGE_D}");

    // print multiple static strings as positional and inline
    println!("{}, {MESSAGE_F}", MESSAGE_E);
}
