/*
Functions - reference to immutable as mutable argument

NOTICE -> has lifetime problems
*/

fn do_immutable_some(mut x: &u32) {
    let k: u32 = 222;
    println!("*x bef {}", *x);
    x = &k;  // will not work because of lifetime
    println!("*x aft {}", *x);

}

fn main() {
    let a: u32 = 111;
    do_immutable_some(&a);
}
