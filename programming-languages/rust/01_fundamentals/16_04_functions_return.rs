/*
Functions

Functions can return with 'return <value>' or by simply specifying the value without ';'
at the end.
*/

fn do_this() -> u32 {
    println!("calling do_this");
    return 123;
}

fn do_that() -> u32 {
    println!("calling do_that");
    777
}

fn do_bla() -> u32 {
    println!("calling do_bla");
    let x = 999;
    x
}


fn main() {
    let mut k: u32;

    k = do_this();
    println!("value from do_this: {}", k);

    k = do_that();
    println!("value from do_that: {}", k);

    k = do_bla();
    println!("value from do_bla: {}", k);
}
