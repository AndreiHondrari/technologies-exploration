mod bar;
mod foo;
mod kek; // <- inside KEK is the {self, something} syntax used

use self::bar::do_other;
use foo::do_some;

fn main() {
    println!("Hello, world!");

    // from foo
    do_some();

    // from bar
    do_other();
}
