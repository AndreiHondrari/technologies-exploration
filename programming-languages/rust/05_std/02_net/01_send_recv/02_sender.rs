use std::io::prelude::*;
use std::net::*;
use std::thread;
use std::time::Duration;

fn main() {
    println!("[SNDR] START");

    println!("[SNDR] CONNECT");

    // open a connection to the listener
    let mut stream = TcpStream::connect("127.0.0.1:56789").unwrap();

    let mut val = 1;

    // send messages in a loop
    loop {
        // compose the message
        let msg = String::from(format!("hello {val}"));
        println!("[SNDR] sending {msg} ...");

        // put the message in the buffer
        stream.write(msg.as_bytes()).ok();

        thread::sleep(Duration::from_millis(500));
        val += 1;
    }
}
