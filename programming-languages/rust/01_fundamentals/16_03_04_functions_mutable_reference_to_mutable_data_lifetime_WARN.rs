/*
Functions - references as argument - mutable

Mutable references can be used to change the value outside of the function.

There is a distinction between the mutability of the data being referenced and
the mutability of the function parameter itself.
*/

#[allow(unused_mut)] // to silence to compiler about no mutation
fn do_immutable_some(mut x: &u32) {
    println!("do_immutable_some {}", x);
}

#[allow(unused_mut)] // to silence to compiler about no mutation
fn do_mutable_some(mut x: &mut u32) {
    println!("do_mutable_some BEF {}", x);
    *x = 777;
    println!("do_mutable_some AFT {}", x);
}

fn main() {
    let mut k: u32 = 123;

    do_immutable_some(&k);
    do_mutable_some(&mut k);
    println!("K after mutable call: {}", k);
}
