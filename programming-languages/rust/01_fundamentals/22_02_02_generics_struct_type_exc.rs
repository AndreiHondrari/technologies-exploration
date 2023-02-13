/*
Generics - struct attributes with generic type
*/

struct Foo<T> {
    x: T
}

fn main() {
    let v: i16 = 123;

    // WILL NOT WORK
    let f1: Foo<u8> = Foo {x: v};

    println!("{}", f1.x);
}
