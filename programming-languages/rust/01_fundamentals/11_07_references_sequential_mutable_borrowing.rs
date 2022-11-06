/*
References

A reborrow palindrome is a scope layout where a borrowed reference can be used only
after the borrowing scope ends.
*/


fn main() {

    let mut x: i32 = 111;

    /* ┌─ */ let _a: &mut i32 = &mut x;
    /* └─ */ println!("{}", _a);

    x = 222;

    /* ┌─ */ let _b: &mut i32 = &mut x;
    /* └─ */ println!("{}", _b);
}
