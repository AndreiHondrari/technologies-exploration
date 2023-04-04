/*
smart pointers - reference count
*/


use std::rc::Rc;

#[derive(Debug)]
struct Node;


fn main() {

    let a: Rc<u16> = Rc::new(123);  // 1 ref
    println!("ref count before scope {}", Rc::<u16>::strong_count(&a));

    {
        println!("entering scope");

        let _b: Rc<u16> = Rc::clone(&a); // 2 ref
        println!("ref count inside scope {}", Rc::<u16>::strong_count(&a));

        println!("exiting scope");
    }

    println!("ref count after scope {}", Rc::<u16>::strong_count(&a));


}
