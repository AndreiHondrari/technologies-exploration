/*
common traits - default
*/

#[derive(Debug)]
struct Some {
    x: u16,
    y: u16
}

impl Default for Some {
    fn default() -> Self {
        Self {x: 11, y: 22}
    }
}

fn main() {
    // calling default directly from Some
    let a: Some = Some::default();
    println!("A | {:?}, {:?}", a.x, a.y);

    // calling common default function
    let b: Some = Default::default();
    println!("B | {:?}, {:?}", b.x, b.y);
}
