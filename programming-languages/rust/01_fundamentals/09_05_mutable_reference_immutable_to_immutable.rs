/*
References

NOTICE that here the reference variable itself is mutable,
and it is not the reference it is pointing to that is mutable.
*/


fn main() {
    let a: i32 = 111;
    let b: i32 = 222;

    let mut x: &i32 = &a;
    println!("#1 X: {}", x);

    x = &b;
    println!("#2 X: {}", x);
}
