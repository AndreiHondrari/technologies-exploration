/*
smart pointers - clone before drop
*/


// NOTICE the Clone
#[derive(Debug, Clone)]
struct Something {
    name: String
}

impl Drop for Something {
    fn drop(&mut self) {
        println!("Dropping ...");
    }
}

fn main() {
    println!("Before scope");

    {
        println!("Entering scope");

        // instantiate s1
        let s1 = Something {name: String::from("Gandalf")};

        // clone s1 to s2 (now there are two values in memory)
        let s2 = s1.clone();

        println!("names -> {} {}", s1.name, s2.name);

        // move s1 and release the memory
        drop(s1);

        // let s3 = s1;  // WILL NOT WORK
        println!("S2 -> {:?}", s2);
        println!("Exiting scope");
    }

    println!("After scope")
}
