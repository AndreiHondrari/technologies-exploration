/*
References

References can immutably reference mutable variables.
*/


fn main() {
    let mut _x = 123;
    let y: &i32 = &_x;

    println!("Y {}", y);
}
