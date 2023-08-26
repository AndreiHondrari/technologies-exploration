/*

*/

use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel::<bool>();

    let thread_a = thread::spawn(move || {
        println!("[TH A] START");

        println!("[TH A] wait for thread B ...");
        rx.recv_timeout(Duration::from_secs(3)).ok();

        println!("[TH A] END");
    });

    let thread_b = thread::spawn(move || {
        println!("[TH B] START");

        println!("[TH B] wait a bit ...");
        thread::sleep(Duration::from_secs(2));

        println!("[TH B] send signal ...");
        tx.send(true).unwrap();

        println!("[TH A] END");
    });

    thread_a.join().ok();
    thread_b.join().ok();
}
