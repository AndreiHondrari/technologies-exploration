/*
Structs - as tuples

Struct can define named tuples.
*/


fn main() {
    struct Something(u32, u32);

    let x = Something(11, 22);
    println!("{} {}", x.0, x.1);
}
