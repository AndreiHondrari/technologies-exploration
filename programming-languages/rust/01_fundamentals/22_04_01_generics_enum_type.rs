/*
Generics - enum options with generic type
*/

#[derive(Debug)]
enum Gandalf<T> {
    Foo(T),
    Bar
}

fn main() {
    let p1: Gandalf<u8> = Gandalf::Foo(123);
    println!("{:?}", p1);

    // ignore
    let _k: Gandalf<u8> = Gandalf::Bar;
}
