/*
Borrowing a mutable variable as a reference is
allowed only once in a given scope.

You can borrow multiple times by scoping.
*/

fn main() {
    // define a mutable variable
    let mut x = 123;

    // open a scope
    {
        // first reference of the mutable variable
        let r1 = &mut x;

        // use the first reference
        let v1 = r1;
        println!("{}", v1);
    }  // r1 is released at the end of the scope

    // second reference of the mutable variable
    let r2 = &mut x;

    // use the second reference
    let v2 = r2;
    println!("{}", v2);
}
