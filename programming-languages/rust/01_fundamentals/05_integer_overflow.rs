/*
Adding over the maximum of an integer
by default results in an error,
that makes you acknowledge that fact.

It is possible to safely add by
starting from 0 with the special method wrapping_add(value).
This means you are purposefully performing
this operation.
*/

fn main() {
    let k: u8 = 255;
    println!("original  {}", k);

    // special method to not panic when adding
    let x: u8 = k.wrapping_add(3);
    println!("x         {}", x);

    // non-wrapped panicking add
    println!("Try defining y ...\n");
    let y: u8 = k + 1;
    println!("y         {}", y);
}
