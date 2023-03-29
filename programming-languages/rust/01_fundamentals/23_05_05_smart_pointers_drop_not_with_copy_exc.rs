/*
smart pointers - Copy does not work for types with destructors

You can't define a copy operation on a type that has a destructor
because the purpose of the destructor is to free the memory
allocated within the type, and copying inherently means that
the pointer of that dynamically allocated data will be copied
which can result in a double free.

Drop with Clone however works, because cloning implies that
the data is copied to a new area of memory, that has
a separate memory management.
*/


#[derive(Debug)]
struct Something {
    k: u32
}

impl Drop for Something {
    fn drop(&mut self) {
        println!("Dropping ...");
    }
}

// Implementing Copy for a type with a destructor (drop)
// will result in a compilation error
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
        let _s1 = Something {k: 111};
        println!("Exiting scope");
    }

    println!("After scope")
}
