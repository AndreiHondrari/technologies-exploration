/*
Scope - shadowing variables from outer scope
*/

fn main() {
    let something = 111;

    {
        // temporarily (for the current scope)
        // shadow the outside variable
        // with the same identifier
        let something = 222;
        println!("A | {something}");
    }

    // unaffected by the inner scope
    println!("B | {something}");
}
