/*
Threads - builder
*/

use std::thread;

fn do_some() {
    let current = thread::current();
    let name = current.name().unwrap();
    println!("Hello from thread {name}");
}

fn main() {
    /*
    spawn threads using a builder factory
    to configure the threads
    */
    let thread_a = thread::Builder::new()
        .name("aaa".into())
        .spawn(&do_some)
        .unwrap();

    let thread_b = thread::Builder::new()
        .name("bbb".into())
        .spawn(&do_some)
        .unwrap();

    thread_a.join().ok();
    thread_b.join().ok();
}
