/*
Functions as output
*/



fn my_func(
    message: &str
) -> fn() {
    return || {
        println!("calling inside");
    };
}

fn main() {
    let f1 = my_func("AAA");
    let f2 = my_func("BBB");

    println!("CALL F1");
    f1();

    println!("CALL F2");
    f2();
}
