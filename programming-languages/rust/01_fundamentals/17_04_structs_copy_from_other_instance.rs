/*
Structs

Struct update syntax
*/


fn main() {
    struct Something {
        a: u32,
        b: bool,
        c: f32
    }

    let o1: Something = Something {
        a: 123,
        b: false,
        c: 6.28
    };

    let o2: Something = Something {
        a: 777,
        ..o1  // NOTICE the struct update syntax here
    };

    println!("O1 {} {} {}", o1.a, o1.b, o1.c);
    println!("O2 {} {} {}", o2.a, o2.b, o2.c);
}
