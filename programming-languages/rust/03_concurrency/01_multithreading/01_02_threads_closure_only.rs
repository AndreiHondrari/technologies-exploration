/*
Threads - closure spawn
*/

use std::thread;
use std::time::Duration;

fn main() {
    /*
    pass closures with the thread code
    directly to the spawner function
    */

    // a slightly more complicated thread
    let thread_a = thread::spawn(|| {
        let duration = Duration::from_millis(200);

        // do multiple things inside the thread (with a delay)
        for i in 1..5 {
            println!("[THREAD AAA] {i}");
            thread::sleep(duration);
        }
    });

    // a simple thread
    let thread_b = thread::spawn(|| println!("[THREAD BBB] doing aaand ...done"));

    // wait for threads to finish
    thread_a.join().ok();
    thread_b.join().ok();
}
