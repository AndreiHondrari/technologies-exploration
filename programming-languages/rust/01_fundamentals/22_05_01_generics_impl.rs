/*
generics - impl for annotated generic type

When defining some methods for a type,
you can specify for which type annotation
the impl block is implementing those methods.
*/


struct Foo<T> {
    x: T
}

impl Foo<u8> {
    fn give_this(&self) -> u8 {
        self.x
    }
}

impl Foo<i32> {
    fn give_that(&self) -> i32 {
        self.x
    }
}

fn main() {
    let a: Foo<u8> = Foo {x: 11};
    let b: Foo<i32> = Foo {x: 22};

    let k = a.give_this();  // for u8
    let p = b.give_that();  // for i32

    println!("{}, {}", k, p);

    // WILL NOT WORK
    // let _z = a.give_that()
}
