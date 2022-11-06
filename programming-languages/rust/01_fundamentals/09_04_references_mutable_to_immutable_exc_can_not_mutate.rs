/*
References

References can not point to immutable data as mutable.
*/


fn main() {
    let x: i32 = 123;
    let y: &mut i32 = &mut x;  // it does not make sense to mutate immutable data

    println!("{}", y);
}
