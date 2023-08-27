mod child_mod;

pub fn do_something(msg: String) {
    child_mod::do_kek(msg.clone());
    println!("[{msg}] doing something from module something ...");
}
