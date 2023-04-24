/*
common traits - clone

Purpose of clone is
to provide a mechanism to duplicate information
when the process of duplication is not straight forward.

It is particularly relevant for data
allocated dynamically.

It differs from Copy in the sense that
some types are not elligible or not meant
to be deeply copied.

Another difference is that
Copy can be implemented for types
that hold values which all of them implement Copy.
Clone does not require that.
*/

#[derive(Debug)]
struct Some {
    x: u16,
    y: u16
}

impl Clone for Some {
    fn clone(&self) -> Some {
        Some{x: self.x, y: self.y}
    }
}

fn main() {
    let mut s1 = Some{x: 11, y: 22};
    println!("S1 original \t{:?}", s1);

    // gets a totally new instance of Some
    // the two objects are independent
    let s2 = s1.clone();
    println!("S2 original \t{:?}", s2);

    println!("-> Change S1");
    s1.x = 333;

    println!("S1 after \t{:?}", s1);
    println!("S2 after \t{:?}", s2);
}
