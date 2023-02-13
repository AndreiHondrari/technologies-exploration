/*
Generics - struct attributes with generic type
*/

struct Foo<T> {
    x: T
}

fn main() {
    let f1: Foo<u8> = Foo {x: 123};

    println!("{}", f1.x);
}
