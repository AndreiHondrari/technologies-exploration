/*
Functions - Closures

Closures that are mutable can only be defined in an enclosed ownership scope
that doesn't intersect with an immutable borrow
*/


fn main() {

                let mut x = 123;
                let mut _y = x;  // to silence the compiler

                println!("non-mutated x\t {}", x);

                // notice the extra 'mut' in front of the closure name
    /* ┌──── */ let mut my_func = || {
    /* │     */    x = 555;  // mutates outside x
    /* │     */ };
    /* │     */
    /* └──── */ my_func();

                println!("mutated x\t {}", x);

}
