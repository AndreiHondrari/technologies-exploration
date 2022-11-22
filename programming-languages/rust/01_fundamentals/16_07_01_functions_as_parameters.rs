/*
Functions as parameters
*/

fn f1() {
    println!("calling f1 ...");
}

fn f2() {
    println!("calling f2 ...");
}

fn my_func(
    message: &str,
    some_f: fn()
) {
    println!("my_func: {message}");
    some_f();
}

fn main() {
    my_func("XXX", f1);
    my_func("ZZZ", f2);
}
