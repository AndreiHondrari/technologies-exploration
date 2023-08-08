/*
Threads - closure spawn
*/

use std::thread;
use std::time::Duration;

fn main() {
    let thread_a = thread::spawn(|| {
        let duration = Duration::from_millis(200);

        for i in 1..5 {
            println!("[THREAD AAA] {i}");
            thread::sleep(duration);
        }
    });

    let thread_b = thread::spawn(|| {
        println!("[THREAD BBB] doing aaand ...done")
    });

    thread_a.join().ok();
    thread_b.join().ok();
}
