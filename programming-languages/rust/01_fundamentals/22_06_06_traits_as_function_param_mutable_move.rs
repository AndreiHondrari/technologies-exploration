/*
generic - traits - mutable move impl as function parameter
*/

trait TraitKek {
    fn do_some(&mut self);
    fn show(&self) -> String;
}

struct Foo {
    x: u16,
}

impl TraitKek for Foo {
    fn do_some(&mut self) {
        self.x += 11;
    }

    fn show(&self) -> String {
        String::from(format!("{}", self.x))
    }
}

fn alter_thing(mut obj: impl TraitKek) -> impl TraitKek {
    obj.do_some();
    obj
}

fn main() {
    let foo = Foo { x: 11 };
    println!("[pre]\t{}", foo.show());
    let zar = alter_thing(foo);
    // foo no longer usable here because it was moved as alter_thing
    println!("[post]\t{}", zar.show());
}
