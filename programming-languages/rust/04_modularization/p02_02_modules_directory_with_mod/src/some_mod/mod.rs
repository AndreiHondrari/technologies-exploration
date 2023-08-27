fn do_kek(msg: String) {
    println!("[{msg}] doing kek ...")
}

pub fn do_something(msg: String) {
    do_kek(msg.clone());
    println!("[{msg}] doing something from module something ...");
}
