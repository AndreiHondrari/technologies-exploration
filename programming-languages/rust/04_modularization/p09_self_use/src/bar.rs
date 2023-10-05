use crate::kek::{self, do_kek}; // NOTICE <-- the self

pub fn do_other() {
    println!("do other ...");
    do_kek();
    kek::do_lol();
}
