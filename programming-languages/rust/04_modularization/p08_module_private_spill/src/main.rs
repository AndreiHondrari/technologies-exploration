/*
Modules - private spill - DOES NOT COMPILE
*/

#[allow(dead_code)]
mod potato {
    // NOTICE this struct is private
    #[derive(Debug)]
    struct Foo {
        x: u16,
    }

    // NOTICE this function uses a private structure type
    // DOES NOT COMPILE because of it
    pub fn do_some(thing: Foo) {
        println!("{thing:?}");
    }
}

fn main() {
    println!("dummy print");
}
