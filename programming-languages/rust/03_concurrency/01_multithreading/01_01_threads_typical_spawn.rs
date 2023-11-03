/*
Threads - simple spawn
*/

use std::thread;
use std::time::Duration;

// declare our thread handler function
fn do_some(delay: u16, name: String) {
    let duration = Duration::from_millis(delay.into());

    // do multiple things inside the thread (with a delay)
    for i in 1..5 {
        println!("[{name}] {i}");
        thread::sleep(duration);
    }
}

fn main() {
    // spawn threads
    let thread_a = thread::spawn(|| {
        do_some(700, String::from("thread-A"));
    });
    let thread_b = thread::spawn(|| {
        do_some(100, String::from("thread-B"));
    });

    // wait for threads to finish
    thread_a.join().ok();
    thread_b.join().ok();
}
