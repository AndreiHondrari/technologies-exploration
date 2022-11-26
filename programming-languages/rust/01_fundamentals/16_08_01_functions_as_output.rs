/*
Functions as output
*/

fn some_f() {
    println!("calling some_f ...");
}

fn my_func() -> fn() {
    println!("calling my_func ...");
    return some_f;
}


fn main() {
    let f1 = my_func();
    let f2 = my_func();

    println!("CALL F1");
    f1();

    println!("CALL F2");
    f2();
}
