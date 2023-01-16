/*
Structs

Struct update syntax
*/


fn main() {
    struct Foo {
        a: u32,
        b: u32,
    }

    struct Bar {
        inner_foo: Foo
    }

    struct Kek {
        inner_bar: Bar
    }

    let o1: Foo = Foo {
        a: 11,
        b: 22
    };

    let o2: Bar = Bar {
        inner_foo: o1,
    };

    let o3: Kek = Kek {
        inner_bar: o2
    };

    println!(
        "{} {}",
        o3.inner_bar.inner_foo.a,
        o3.inner_bar.inner_foo.b
    );
}
