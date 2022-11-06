/*
References

Many immutable borrows can occur
*/


fn main() {

    /*
    ##################################################################
    STEP 1 - Declare a mutable variable
    ##################################################################
    */
    let mut x: i32 = 111;

    /*
    ##################################################################
    STEP 2 - Borrow as immutable many times

    declaration of a, b and c
    x loses ownership multiple times (immutable borrowing counter++)
    a, b and c gain ownership subsequently
    ##################################################################
    */
    let a: &i32 = &x;
    let b: &i32 = &x;
    let c: &i32 = &x;

    /*
    ------------------------------------------------------------------
    Observation: x CAN NOT mutate here because x is borrowed (at least once)
    ------------------------------------------------------------------
    */
    // x = 777;  // -> WILL NOT WORK

    /*
    ##################################################################
    STEP 3 - Release ownership back to x

    last uses of a, b and c
    a, b and c lose ownership
    x gains ownership back
    ##################################################################
    */
    let mut _k: i32 = *a;
    _k = *b;
    _k = *c;

    println!("Final K: {}", _k);

    // ### IGNORE ###
    // mutate x so that the compiler will not complain
    x = 222;

    // ### IGNORE ###
    // use x so that the compiler will not complain
    let _nul: i32 = x;
}
