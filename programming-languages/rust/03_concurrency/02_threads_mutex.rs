/*
Threads - Mutex
*/

use std::thread;

use std::time::Duration;

use std::sync::Arc;
use std::sync::LockResult;
use std::sync::Mutex;
use std::sync::MutexGuard;

fn do_some(shared_thing: Arc<Mutex<u16>>, upper_limit: u16) {
    let current = thread::current();
    let name = current.name().unwrap();

    // do some things inside the thread
    for _ in 0..upper_limit {
        {
            let locked_thing: LockResult<MutexGuard<u16>> = shared_thing.lock();
            let mut value: MutexGuard<u16> = locked_thing.unwrap();
            *value += 1;
            let x = *value;
            println!("[{name}] increments to {x}");
        }
        thread::sleep(Duration::from_millis(100));
    }
}

fn main() {
    // declare shared data
    let original_shared_rc: Arc<Mutex<u16>> = Arc::new(Mutex::<u16>::new(0));

    // create thread-safe references to the shared data
    let shared_thing_for_a = Arc::clone(&original_shared_rc);
    let shared_thing_for_b = Arc::clone(&original_shared_rc);

    // declare first thread to operate on the shared data
    let thread_a = thread::Builder::new()
        .name("thread-A".into())
        .spawn(move || do_some(shared_thing_for_a, 10))
        .unwrap();

    // declare second thread to operate on the shared data
    let thread_b = thread::Builder::new()
        .name("thread-B".into())
        .spawn(move || do_some(shared_thing_for_b, 7))
        .unwrap();

    // wait for threads to finish
    thread_a.join().unwrap();
    thread_b.join().unwrap();

    // inspect final value of the shared data
    let value = { *original_shared_rc.lock().unwrap() };

    println!("[MAIN] -> {value}")
}
