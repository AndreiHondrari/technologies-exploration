use std::io::prelude::*;
use std::net::*;
use std::thread;
use std::time::Duration;

fn handle_stream(mut stream: TcpStream) {
    let peer_address = stream.peer_addr().unwrap();
    let addr = peer_address.to_string();

    println!("[CONNECT]\t {addr}");

    let mut buffer = [0; 50];
    let mut first_run = true;
    let mut recv_size: usize = 0;
    let mut content = String::new();

    while first_run ^ (recv_size != 0) {
        content.clear();
        first_run = false;
        recv_size = stream.read(&mut buffer).unwrap();
        println!("{buffer:?}");
        for byte in buffer {
            if byte == 0 {
                break;
            };
            content.push(byte.into());
        }
        println!("{content:?}\n");
    }

    println!("[{addr}] GOODBYE!");
}

fn main() {
    println!("[RECV] START");

    println!("[RECV] bind ...");
    let listener = TcpListener::bind("127.0.0.1:56789").unwrap();

    println!("[RECV] start listening ...");
    for stream in listener.incoming() {
        handle_stream(stream.unwrap());
    }

    println!("[RECV] FIN");
}
