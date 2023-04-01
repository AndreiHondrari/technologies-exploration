/*
Smart pointers - RefCell basic functionality
*/

use std::cell::RefCell;
use std::cell::RefMut;


fn main() {
    // wrap a value in a RefCell
    let x: RefCell<u32> = RefCell::new(123);
    println!("{:?}", x);

    // obtain an immutable reference to the RefCell instance
    let y: &RefCell<u32> = &x;

    /*
    Using a scope because RefMut are not dropped automatically
    after borrowing.

    This is a characteristic of the structures associated with RefCell,
    that circumvent compilation borrow scope checks.
    */
    {
        // use the immutable reference to borrow a mutable variant
        // of the value within the RefCell instance
        let mut q: RefMut<u32> = y.borrow_mut();
        *q = 222;
    }  // RefMut is dropped here (achieveable with drop(...) as well)

    // NOTICE: the changed value (even though originally it was declared immutable)
    println!("{:?}", x);
}
