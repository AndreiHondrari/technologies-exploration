/*
Moving - immutable as mutable

Moving allows for an old variable to become something else.

pass/move a struct instance to a function (immutable -> mutable)
*/

#[allow(dead_code)]
#[derive(Debug)]
struct Foo {
    x: u16,
}

impl Foo {
    fn change_me(&mut self) {
        println!("{self:?} | change_me");
        self.x = 222;
    }
}

fn alter(mut obj: Foo) -> Foo {
    obj.change_me();
    obj
}

fn main() {
    let original = Foo { x: 111 };
    println!("Original {original:?}");

    let new_thing = alter(original);
    println!("New thing {new_thing:?}");
}
