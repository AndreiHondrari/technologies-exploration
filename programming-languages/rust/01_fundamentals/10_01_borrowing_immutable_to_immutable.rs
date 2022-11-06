/*
Borrowing

Observation: not using prinln because it also borrows,
             and the purpose is to have a pristine example
*/

fn main() {
    let x: i32 = 1234;

    let a: &i32 = &x;  // x is borrowed to a

    let _k: &i32 = &x;  // reborrow of x to _k
    let _p: &i32 = &a;  // reborrow of a to _p (after x is reborrowed)
}
