/*
Structs
*/


fn main() {
    struct Something {
        a: u32,
        b: bool
    }

    let o1: Something = Something {
        a: 123,
        b: true
    };

    println!("{}", o1.a);
    println!("{}", o1.b);

}
