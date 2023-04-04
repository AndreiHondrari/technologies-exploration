/*
Smart pointers - RefCell - auto deref
*/

use std::cell::RefCell;
use std::cell::Ref;

trait DoSome {
    fn do_some(&self);
}

struct Foo;

impl DoSome for Foo {
    fn do_some(&self) {
        println!("Doing something");
    }
}

fn main() {
    let foo_cell: RefCell<Foo> = RefCell::new(Foo);  // wrap instance in RefCell
    let foo_ref: Ref<Foo> = foo_cell.borrow();  // get the instance reference
    foo_ref.do_some();  // automatically dereference
}
