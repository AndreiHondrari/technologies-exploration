/*
Generics - infer with underscore annotation
*/

struct Foo<T> {
    x: T,
}

fn main() {
    // NOTICE the underscore in the <> type annotation
    let f1: Foo<_> = Foo { x: 123 };

    println!("{}", f1.x);
}
