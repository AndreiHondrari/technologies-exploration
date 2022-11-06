/*
References

A reborrow palindrome is a scope layout where a borrowed reference can be used only
after the borrowing scope ends.
*/


fn main() {

    let mut x: i32 = 111;

    /* ┌──── */ let _a: &mut i32 = &mut x;
    /* │ ┌── */ let _b: &mut i32 = _a;
    /* │ │   */
    /* │ └── */ let mut _k: i32 = *_b;
    /* └──── */ _k = *_a;
}
