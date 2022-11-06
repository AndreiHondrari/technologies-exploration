/*
References

Only one mutable borrow can occur
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
    STEP 2 - Borrow as mutable many times

    declaration of a and b
    x loses ownership
    a gains ownership as mutable
    b CAN NOT gain ownership
    ##################################################################
    */
    let a: &mut i32 = &mut x;
    let b: &mut i32 = &mut x;  // WILL NOT WORK because x already borrowed as mutable by a

    /*
    ##################################################################
    STEP 3 - Release ownership back to x

    last uses of aand b
    a loses ownership
    x gains ownership back
    b never gained ownership in the first place
    ##################################################################
    */
    let mut _k: i32 = *a;
    _k = *b;

    println!("Final K: {}", _k);

    // ### IGNORE ###
    // mutate x so that the compiler will not complain
    x = 222;

    // ### IGNORE ###
    // use x so that the compiler will not complain
    let _nul: i32 = x;
}
