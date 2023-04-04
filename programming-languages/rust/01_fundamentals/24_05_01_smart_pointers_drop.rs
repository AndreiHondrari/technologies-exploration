/*
smart pointers - drop (sort of destructor)
*/


struct Something {
    name: String
}

impl Drop for Something {
    fn drop(&mut self) {
        println!("{} going out", self.name)
    }
}

fn main() {
    println!("Before scope");

    {
        println!("Entering scope");
        let _s1 = Something {name: String::from("Gandalf")};
        println!("Exiting scope");
    }

    println!("After scope")
}
