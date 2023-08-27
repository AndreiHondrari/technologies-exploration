/*
The actual module definition.

NOTICE
    - there is also a some_mod directory
    - there is no mod.rs in some_mod
*/

mod child_mod;

pub fn do_something(msg: String) {
    child_mod::do_kek(msg.clone());
    println!("[{msg}] doing something from module something ...");
}
