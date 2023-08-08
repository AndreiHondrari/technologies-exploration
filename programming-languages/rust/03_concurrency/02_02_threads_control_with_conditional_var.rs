/*

*/

use std::sync::Arc;
use std::sync::Condvar;
use std::sync::Mutex;
use std::thread;
use std::time::Duration;

fn do_thread_run(pair_rc: Arc<(Mutex<bool>, Condvar)>) {
    let current = thread::current();
    let name = current.name().unwrap();

    let (mutex, cvar) = &*pair_rc;

    println!("[{name}] START");

    println!("[{name}] wait for master ...");
    let duration = Duration::from_secs(5);
    cvar.wait_timeout(mutex.lock().unwrap(), duration).ok();

    println!("[{name}] END");
}

fn do_master_handle(pair_rc: Arc<(Mutex<bool>, Condvar)>) {
    println!("[MASTER] START");

    let (_mutex, cvar) = &*pair_rc;

    thread::sleep(Duration::from_secs(1));

    println!("[MASTER] NOTIFY ALL");
    cvar.notify_all();

    println!("[MASTER] END");
}

fn main() {
    println!("[MAIN] START");

    let pair_rc = Arc::new((Mutex::new(true), Condvar::new()));

    // slave threads
    let mut handlers = vec![];
    for i in 0..3 {
        let new_pair_rc = Arc::clone(&pair_rc);
        let new_handler = thread::Builder::new()
            .name(format!("thread-{i}").into())
            .spawn(move || do_thread_run(new_pair_rc))
            .unwrap();

        handlers.push(new_handler);
    }

    // master thread
    let master_thread = thread::spawn(move || do_master_handle(Arc::clone(&pair_rc)));

    master_thread.join().ok();

    for handler in handlers {
        handler.join().ok();
    }
    println!("[MAIN] END");
}
