/*
References

When reborrowing, the scope of the reference that reborrows must end before
using the first reference.
*/


fn main() {

    let mut x: i32 = 111;

    /* ┌──── */ let _a: &mut i32 = &mut x;
    /* │ ┌── */ let _b: &mut i32 = _a;
    /* │ │   */
    /* └──── */ let mut _k: i32 = *_a;  // WILL NOT WORK - use of reborrowed reference
    /*   │   */
    /*   └── */ _k = *_b; // this is where _b's reborrow scope actually ends
}
