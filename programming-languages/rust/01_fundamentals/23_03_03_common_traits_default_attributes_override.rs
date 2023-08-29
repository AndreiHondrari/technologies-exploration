/*
common traits - default - override specific defaults
*/

use std::default::*;

#[allow(dead_code)]
#[derive(Debug)]
enum SomeKind {
    STALIN,
    GANDALF,
    DUMBLEDORE,
}

impl Default for SomeKind {
    fn default() -> Self {
        SomeKind::STALIN
    }
}

#[allow(dead_code)]
#[derive(Debug)]
struct Some {
    x: u16,
    y: i32,
    kind: SomeKind,
}

/*
Necessary to have Default for Some
due to the use of ..Default::default() in the constructor
*/
impl Default for Some {
    fn default() -> Self {
        Self {
            x: 111,
            y: 222,
            kind: SomeKind::GANDALF,
        }
    }
}

fn main() {
    let s1: Some = Some {
        x: 777,               // override x
        ..Default::default()  // keep the rest of defaults from Some::default
    };
    println!("{:?}", s1);
}
