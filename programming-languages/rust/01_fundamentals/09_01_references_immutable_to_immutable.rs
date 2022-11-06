/*
References

A reference is simply using the same memory as the variable that was referenced
*/


fn main() {
    let _x: i32 = 123;
    let y: &i32 = &_x;

    println!("{}", y);
}
