/*
this crate must declare
both modules.

foo will use bar for some internal action
*/
mod bar;
mod foo;

fn main() {
    foo::do_foo();
}
