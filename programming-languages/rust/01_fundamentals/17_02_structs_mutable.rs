/*
Structs

Attributes of structs can be changed if the struct instance is mutable.
*/


fn main() {
    struct Something {
        a: u32,
        b: bool
    }

    let mut o1: Something = Something {
        a: 123,
        b: true
    };

    println!("BEF {} {}", o1.a, o1.b);

    o1.a = 222;

    println!("AFT {} {}", o1.a, o1.b);

}
