/*
Borrowing a mutable variable as a reference is
allowed only once in a given scope.
*/

fn main() {
    // define a mutable variable
    let mut x = 123;

    // first reference of the mutable variable
    let r1 = &mut x;

    // second reference of the mutable variable (illegal!)
    let r2 = &mut x;

    let v1 = x;  //
    let v2 = r1;
    let v3 = r2;

    // just show values
    println!("{}", v1);
    println!("{}", v2);
    println!("{}", v3);
}
