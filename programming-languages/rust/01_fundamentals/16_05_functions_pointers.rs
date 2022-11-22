/*
Functions


*/

fn do_this() {
    println!("calling do_this");
}

fn do_that() {
    println!("calling do_that");
}


fn main() {
    let mut my_func: fn();

    my_func = do_this;
    my_func();

    my_func = do_that;
    my_func();
}
