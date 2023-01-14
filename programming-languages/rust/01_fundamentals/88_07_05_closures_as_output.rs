/*
Functions as output
*/



fn my_func() -> fn() {
    return || {
        println!("calling inside");
    };
}

fn main() {
    let f1 = my_func();
    let f2 = my_func();

    println!("CALL F1");
    f1();

    println!("CALL F2");
    f2();
}
