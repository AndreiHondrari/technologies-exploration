/*
Generics - enum options with generic type
*/

#[derive(Debug)]
enum Gandalf<T> {
    Foo(T)
}

fn main() {
    let mut _k: Gandalf<u8> = Gandalf::Foo(11);

    let p: i32 = 22;
    _k = Gandalf::Foo(p);  // WILL NOT WORK
}
