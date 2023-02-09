/*
Scope - variables exist only in a given scope

Scope is defined by brackets
*/

fn main() {
    let x = 111;

    {
        let y = 222;

        // x and y both available here
        println!("A | {x} | {y}");
    }

    // only x available here
    // let _k = y;  // WILL NOT WORK because y out of scope
}
