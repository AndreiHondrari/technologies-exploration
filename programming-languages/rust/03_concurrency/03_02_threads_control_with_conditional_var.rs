/*

*/

use std::thread;

use std::sync::Arc;
use std::sync::Condvar;
use std::sync::LockResult;
use std::sync::Mutex;
use std::sync::MutexGuard;

use std::time::Duration;

fn do_thread_run(pair_rc: Arc<(Mutex<bool>, Condvar)>) {
    let current = thread::current();
    let name = current.name().unwrap();

    println!("[{name}] START");

    // unfold the mutex and the condvar
    let (mutex, cvar) = &*pair_rc;

    // lock the associated mutex
    let lock_result: LockResult<MutexGuard<bool>> = mutex.lock();
    let unwrapped_guard: MutexGuard<bool> = lock_result.unwrap();

    println!("[{name}] wait for master ...");
    let timeout_duration = Duration::from_secs(5);
    // when calling wait, the unwrapped guard is released
    let result = cvar.wait_timeout(unwrapped_guard, timeout_duration);

    if result.is_err() {
        println!("[{name}] timed out!")
    }

    println!("[{name}] END");
}

fn do_master_handle(pair_rc: Arc<(Mutex<bool>, Condvar)>) {
    println!("[MASTER] START");

    let (_mutex, cvar) = &*pair_rc;

    // dummy wait to demonstrate
    // that slave threads will not continue
    // until timeout or notification
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
