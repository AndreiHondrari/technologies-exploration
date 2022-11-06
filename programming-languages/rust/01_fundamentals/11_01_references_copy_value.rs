/*
References

Copy value by dereferencing
*/


fn main() {
    let a: i32 = 123;
    let x: &i32 = &a;  // borrow occurs here
    let p: i32 = *x;  // copy occurs here (by dereferencing)

    println!("{}", p);
}
