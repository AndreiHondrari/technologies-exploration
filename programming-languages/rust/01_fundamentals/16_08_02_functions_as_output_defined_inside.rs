/*
Functions as output
Defined inside the provider function
*/


fn my_func() -> fn() {
    println!("calling my_func ...");

    fn some_f() {
        println!("calling some_f ...");
    }
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
