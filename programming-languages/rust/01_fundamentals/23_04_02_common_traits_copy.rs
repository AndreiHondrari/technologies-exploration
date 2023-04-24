/*
common traits - copy

Copy requires Clone.
*/

#[allow(dead_code)]
#[derive(Debug)]
struct Some {
    x: u16,
    y: u16
}

impl Clone for Some {
    fn clone(&self) -> Some {
        // notice we are returning a copy of self
        // and this is not a move operation
        *self
    }
}

impl Copy for Some {}

fn main() {
    let mut s1 = Some{x: 11, y: 22};
    println!("S1 original \t{:?}", s1);

    // gets a totally new instance of Some
    // the two objects are independent
    let s2 = s1;
    println!("S2 original \t{:?}", s2);

    println!("-> Change S1");
    s1.x = 333;

    println!("S1 after \t{:?}", s1);
    println!("S2 after \t{:?}", s2);
}
