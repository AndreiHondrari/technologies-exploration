/*
Moving - immutable as immutable

Moving allows for an old variable to become something else.

pass/move a struct instance to a function (mutable -> mutable)
*/

#[allow(dead_code)]
#[derive(Debug)]
struct Foo {
    x: u16,
}

impl Foo {
    fn change_me(&mut self) {
        println!("{self:?} | change_me");
        self.x = 333;
    }
}

fn alter(mut obj: Foo) -> Foo {
    obj.change_me();
    obj
}

fn main() {
    let mut original = Foo { x: 111 };
    println!("Original {original:?}");

    original.x = 222;

    let new_thing = alter(original);
    println!("New thing {new_thing:?}");
}
