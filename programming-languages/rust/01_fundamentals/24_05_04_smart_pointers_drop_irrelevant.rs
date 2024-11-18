/*
smart pointers - drop irrelevant for primitives and Copy
*/

#[derive(Debug)]
struct Something {
    k: u32,
}

impl Copy for Something {}
impl Clone for Something {
    fn clone(&self) -> Self {
        *self
    }
}

fn main() {
    println!("Before scope");

    {
        println!("Entering scope");

        let s1 = Something { k: 111 };
        let x = 222;

        println!("About to drop!!");

        // does not affect these values
        #[allow(dropping_copy_types)]
        drop(s1);

        #[allow(dropping_copy_types)]
        drop(x);

        // still usable here
        println!("{:?} {:?} {:?}", s1, s1.k, x);

        println!("Exiting scope");
    }

    println!("After scope")
}
