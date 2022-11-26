/*
Structs

A variable with the same name as a parameter of the struct, passed in the initialization
phase, does not require ':'.
*/


fn main() {
    struct Something {
        a: u32,
        b: bool
    }

    let a = 777;  // declare a variable that has the same name like one of the attributes

    let o1: Something = Something {
        a,  // <- NOTICE we just pass the variable (it uses the same identifier)
        b: true
    };

    println!("{} {}", o1.a, o1.b);
}
