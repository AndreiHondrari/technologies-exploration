/*
Scope - variables exist only in a given scope

Explicit use of out of scope variable
*/

fn main() {
    let gandalf = 111;

    {
        let inside_var = 222;

        // x and y both available here
        println!("A | {gandalf} | {inside_var}");
    }

    println!("B | {gandalf}");

    // only x available here
    // WILL NOT WORK because 'inside_var' out of scope
    let _k = inside_var;
}
