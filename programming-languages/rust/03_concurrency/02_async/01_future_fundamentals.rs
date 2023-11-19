/*
Async concurrency - How a future looks behind the scenes

NOTE: This example might not be perfect.
*/
mod special {
    use std::future::Future;
    use std::pin::{pin, Pin};
    use std::sync::{Arc, Mutex};
    use std::task::{Context, Poll, RawWaker, RawWakerVTable, Waker};

    pub struct MyFuture {
        is_ready: Arc<Mutex<bool>>,
    }

    impl MyFuture {
        pub fn new() -> Self {
            let is_ready = Arc::new(Mutex::new(false));

            let is_ready_clone = Arc::clone(&is_ready);
            std::thread::spawn(move || {
                println!("[async subsystem] do some work ...");
                std::thread::sleep(std::time::Duration::from_secs(1));
                println!("[async subsystem] mark done !");

                let mut value_guard = is_ready_clone.lock().unwrap();
                *value_guard = true;
            });

            MyFuture { is_ready: is_ready }
        }
    }

    impl Future for MyFuture {
        type Output = ();

        fn poll(self: Pin<&mut Self>, _cx: &mut Context<'_>) -> Poll<Self::Output> {
            let is_ready = self.is_ready.lock().unwrap();

            return if *is_ready {
                Poll::Ready(())
            } else {
                Poll::Pending
            };
        }
    }

    static VTABLE: RawWakerVTable = RawWakerVTable::new(
        |data| {
            println!("vtable.clone()");
            RawWaker::new(data as *const (), &VTABLE)
        },
        |_data| {
            println!("vtable.wake()");
        },
        |_data| {
            println!("vtable.wake_by_ref()");
        },
        |_data| {
            println!("vtable.drop()");
        },
    );

    pub struct Executor {
        fut: Box<MyFuture>,
    }

    impl Executor {
        pub fn new(fut: MyFuture) -> Self {
            Executor { fut: Box::new(fut) }
        }

        pub fn run(self: &mut Self) {
            println!("executor.run()");
            let mut fut_pin = pin!(&mut *self.fut);
            let waker_data: Box<()> = Box::new(());
            let raw_waker_data: *const () = Box::into_raw(waker_data) as *const ();
            let raw_waker = RawWaker::new(raw_waker_data, &VTABLE);
            let waker = unsafe { Waker::from_raw(raw_waker) };
            let waker: Arc<Waker> = Arc::new(waker);

            let mut cx = Context::from_waker(&*waker);

            loop {
                let result = fut_pin.as_mut().poll(&mut cx);

                match result {
                    Poll::Pending => {
                        println!("executor.run() loop -> PENDING");
                    }

                    Poll::Ready(_) => {
                        println!("executor.run() loop -> READY");
                        break;
                    }
                }

                std::thread::sleep(std::time::Duration::from_millis(500));
            }

            println!("executor.run() after loop");
        }
    }
}

fn main() {
    let fut = special::MyFuture::new();

    let mut executor = special::Executor::new(fut);

    executor.run();
}
