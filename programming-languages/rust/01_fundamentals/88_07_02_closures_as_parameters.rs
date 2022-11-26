/*
Closures as parameters
*/

fn my_func(
    message: &str,
    some_f: fn()
) {
    println!("my_func: {message}");
    some_f();
}

fn main() {
    let x = 10;
    let f1 = || {
        println!("calling f1 ... {x}");
    };

    let f2 = || {
        println!("calling f2 ...");
    };

    my_func("XXX", f1);
    my_func("ZZZ", f2);
}
