/*
Generics - enum options with generic type
*/

#[derive(Debug)]
enum Gandalf<T, U> {
    Foo(T),
    Bar(U)
}

fn main() {
    let a: u8 = 11;
    let b: i32 = 22;

    let mut p1 = Gandalf::Foo(a);
    println!("{:?}", p1);

    p1 = Gandalf::Bar(b);
    println!("{:?}", p1);
}
