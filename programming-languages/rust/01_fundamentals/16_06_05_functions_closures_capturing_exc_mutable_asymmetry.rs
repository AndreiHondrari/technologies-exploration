/*
Functions - Closures

Closures that are mutable can only be defined in an enclosed ownership scope
that doesn't intersect with an immutable borrow
*/


fn main() {

    /*   ┌── */ let mut x = 123;
    /*   │   */ let mut _y = x;  // to silence the compiler
    /*   │   */
    /*   │   */ // notice the extra 'mut' in front of the closure name
    /* ┌──── */ let mut my_func = || {
    /* │ │   */    x = 555;  // mutates outside x
    /* │ │   */ };
    /* │ │   */
    /* │ └── */ let _k: &i32 = &x;
    /* │     */
    /* └──── */ my_func();  // throws error because x is borrowed earlier

}
