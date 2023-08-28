use std::io::prelude::*;
use std::net::*;
use std::thread;
use std::time::Duration;

fn main() {
    println!("[SNDR] START");

    println!("[SNDR] CONNECT");
    let mut stream = TcpStream::connect("127.0.0.1:56789").unwrap();

    let mut val = 1;
    loop {
        let msg = String::from(format!("hello {val}"));
        println!("[SNDR] sending {msg} ...");
        stream.write(msg.as_bytes()).ok();
        // stream.write(&[]).ok();
        stream.flush().ok();

        thread::sleep(Duration::from_millis(500));
        val += 1;
    }

    println!("[SNDR] FIN");
}
