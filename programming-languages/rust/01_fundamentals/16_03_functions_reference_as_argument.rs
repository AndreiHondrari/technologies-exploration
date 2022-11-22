/*
Functions

Can receive mutable and immutable references.
Mutable references can be used to change the value outside of the function.
*/

fn do_immutable_some(x: &u32) {
    println!("do_immutable_some {}", x);
}

fn do_mutable_some(x: &mut u32) {
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
