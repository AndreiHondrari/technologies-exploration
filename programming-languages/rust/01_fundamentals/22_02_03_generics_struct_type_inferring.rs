/*
Generics - struct attributes with generic type

If variable is not annotate with type
when declared, then the attribute of the
struct will have the type inferred from the
passed value.
*/

struct Foo<T> {
    x: T
}

fn main() {
    let v: i16 = 123;
    let f1 = Foo {x: v};
    println!("{}", f1.x);
}
