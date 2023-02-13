/*
Generics - struct attributes with generic type
*/

struct Foo<A, B> {
    x: A,
    y: B
}

fn main() {
    let f1: Foo<u8, i16> = Foo {x: 11, y: 22};

    println!("{}, {}", f1.x, f1.y);
}
