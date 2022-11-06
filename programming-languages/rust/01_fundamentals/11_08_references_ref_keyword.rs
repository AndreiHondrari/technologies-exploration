/*
References

A 'ref' on the left side is the same as an '&' on the right side.
*/


fn main() {
    let x: u32 = 255;

    let ref r1 = x;
    let r2: &u32 = &x;

    println!("{:p}", r1);
    println!("{:p}", r2);
}
