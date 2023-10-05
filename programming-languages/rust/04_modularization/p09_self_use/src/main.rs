mod bar; // <- inside BAR is the {self, something} syntax used
mod foo;
mod kek;

use self::bar::do_other;
use foo::do_some;

fn main() {
    println!("Hello, world!");

    // from foo
    do_some();

    // from bar
    do_other();
}
