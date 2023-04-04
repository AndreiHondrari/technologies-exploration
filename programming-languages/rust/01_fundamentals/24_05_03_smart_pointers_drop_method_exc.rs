/*
smart pointers - calling drop method directly - exception

This will not compile because it is not allowed to call drop method directly.
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
        s1.drop(); // WILL NOT WORK
        println!("Exiting scope");
    }

    println!("After scope")
}
