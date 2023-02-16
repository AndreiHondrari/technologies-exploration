/*
generics - impl for generic type - undefined call

Trying to use a method from an implementation
annotated for a different type will not work.
*/


struct Foo<T> {
    x: T
}

impl Foo<u8> {
    // empty
}

impl Foo<i32> {
    fn give_that(&self) -> i32 {
        self.x
    }
}

fn main() {
    let a: Foo<u8> = Foo {x: 11};

    // WILL NOT WORK
    let _z = a.give_that();
}
