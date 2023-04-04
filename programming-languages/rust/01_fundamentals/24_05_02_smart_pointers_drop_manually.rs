/*
smart pointers - drop manually before the end
*/


struct Something {
    name: String
}

impl Drop for Something {
    fn drop(&mut self) {
        println!("{} going out earlier than expected", self.name)
    }
}

fn main() {
    println!("Before scope");

    {
        println!("Entering scope");
        let s1 = Something {name: String::from("Gandalf")};
        println!("About to drop!!");

        // calling std::mem::drop included with the prelude
        drop(s1);

        println!("Exiting scope");
    }

    println!("After scope")
}
