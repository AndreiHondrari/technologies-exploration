/*
Moving - immutable as immutable

Moving allows for an old variable to become something else.

pass/move a struct instance to a function (mutable -> immutable)
*/

#[allow(dead_code)]
#[derive(Debug)]
struct Foo {
    x: u16,
}

impl Foo {
    fn do_this(&self) {
        println!("{self:?} | do_this");
    }

    fn do_that(&self) {
        println!("{self:?} | do_that");
    }
}

fn do_some(obj: Foo) -> Foo {
    obj.do_this();
    obj.do_that();
    obj
}

fn main() {
    let mut original = Foo { x: 111 };
    println!("Original {original:?}");

    original.x = 222;

    let new_thing = do_some(original);
    println!("New thing {new_thing:?}");
}
