/*
Closures - moving in return
*/

#[allow(dead_code)]
#[derive(Debug)]
struct Foo {
    a: u16,
}

fn main() {
    let x = Foo { a: 123 };
    let my_func = move || x;

    let k = my_func();

    // calling my_func again will not work
    // because x moves out of the closure
    // let p = my_func(); // WILL NOT WORK -> COMPILATION ERROR

    println!("{k:?}");
}
