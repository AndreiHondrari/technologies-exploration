/*
Structs - as mutable tuples

Compared to regular tuples,
struct tuples can be mutable.
*/


fn main() {
    struct Something(u32, u32);

    let mut x = Something(11, 22);
    println!("{} {}", x.0, x.1);
    x.0 = 33;
    println!("{} {}", x.0, x.1);
}
