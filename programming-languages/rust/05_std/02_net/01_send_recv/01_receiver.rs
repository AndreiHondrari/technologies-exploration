use std::io::prelude::*;
use std::net::*;

const DEFAULT_BLOCK_SIZE: usize = 32;

fn handle_stream(mut stream: TcpStream) {
    let peer_address = stream.peer_addr().unwrap();
    let addr = peer_address.to_string();

    println!("[{addr}] CONNECTED");

    // prepare a buffer to take in data from the socket
    let mut buffer = [0; DEFAULT_BLOCK_SIZE];

    let mut content = String::new();

    loop {
        content.clear();

        /*
        pass data from the socket to our buffer.

        read potentially blocks until new data
        is received through the socket.
        */
        let recv_size = stream.read(&mut buffer).unwrap();

        /*
        if nothing is received
        it means the remote socket closed
        */
        if recv_size == 0 {
            break;
        }

        // handle the received bytes
        println!("[{addr}] BUFFER: ");
        for byte in buffer {
            if byte == 0 {
                break;
            };
            content.push(byte.into());
            print!("{byte} ");
        }
        print!("\n");
        println!("[{addr}] {content:?}\n");
    }

    println!("[{addr}] GOODBYE!");
}

fn main() {
    println!("[RECV] START");

    println!("[RECV] bind ...");

    // create a new socket and bind it to a listening address
    let listener = TcpListener::bind("127.0.0.1:56789").unwrap();

    println!("[RECV] start listening ...");

    /*
    block - wait for new connections.
    incoming() returns when there is a new connection.
    loop continuously through new connections.
    */
    for stream in listener.incoming() {
        handle_stream(stream.unwrap());
    }

    println!("[RECV] FIN");
}
