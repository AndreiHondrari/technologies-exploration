/*
Generics - enum options with generic type
*/

#[derive(Debug)]
enum Gandalf<T> {
    Foo(T)
}

fn main() {
    let p1 = Gandalf::Foo(123);
    println!("{:?}", p1);
}
