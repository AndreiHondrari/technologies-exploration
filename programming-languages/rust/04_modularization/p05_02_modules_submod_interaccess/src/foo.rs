// NOTICE the crate:: prefix for importing submod from the root module
use crate::bar;

pub fn do_foo() {
    println!("doing foo");
    bar::do_bar_thing();
}
