/*
smart pointers - reference count
*/


use std::rc::Rc;

#[derive(Debug)]
struct Node;


fn main() {

    let a: Rc<u16> = Rc::new(123);  // 1 ref
    println!("ref count {}", Rc::<u16>::strong_count(&a));

    let b: Rc<u16> = Rc::clone(&a); // 2 ref
    println!("ref count {}", Rc::<u16>::strong_count(&a));

    let c: Rc<u16> = Rc::clone(&a); // 3 ref
    println!("ref count {}", Rc::<u16>::strong_count(&a));

    println!("-> {}, {}, {}", a, b, c);

    println!("drop b & c");
    drop(b);
    drop(c);

    println!("ref count {}", Rc::<u16>::strong_count(&a));

    println!("{:?}", a);
}
