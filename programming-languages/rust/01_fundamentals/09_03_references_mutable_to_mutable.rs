/*
References

References can mutably reference mutable variables.
*/

fn main() {
    let mut x: i32 = 123;
    let y: &mut i32 = &mut x;

    println!("{}", y);
}
