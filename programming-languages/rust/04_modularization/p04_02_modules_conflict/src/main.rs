mod some_mod {
    pub fn do_some() {
        println!("doing AAA ...");
    }
}

fn main() {
    some_mod::do_some();

    /*
    WARNING - does not compile
    because do_bla is not defined
    in the inline mod
    */

    // some_mod::do_bla();  // <-- DOES NOT COMPILE
}
