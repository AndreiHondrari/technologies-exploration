/*
Generics - struct attributes with generic type

Mutating the attribute with inferred type with
a value of a different type it will not work.
*/

struct Foo<T> {
    x: T
}

fn main() {
    let v: u8 = 11;
    let mut f1 = Foo {x: v};

    let _z = f1.x;

    let p: i32 = 22;
    f1.x = p; // WILL NOT WORK
}
