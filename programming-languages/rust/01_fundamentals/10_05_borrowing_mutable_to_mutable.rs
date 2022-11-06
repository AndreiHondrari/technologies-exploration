/*
Borrowing

Observation: not using prinln because it also borrows,
             and the purpose is to have a pristine example
*/

fn main() {

    /*
    ##################################################################
    STEP 1 - declare mutable variable X (ownership belongs to X for now)
    ##################################################################
    */
    let mut x: i32 = 1234;

    // ### IGNORE ###
    // use variable to prevent compiler from complaining before mutation
    let mut _nul: i32 = x;

    /*
    ------------------------------------------------------------------
    Observation: x can mutate before borrowing
    ------------------------------------------------------------------
    */
    x = 111;

    /*
    ##################################################################
    STEP 2 - BORROW => START of borrowing scope

    declaration of y
    x loses ownership
    y gains ownership
    ##################################################################
    */
    let y: &mut i32 = &mut x;  // borrow x to y (ownership belongs to y)

    /*
    ------------------------------------------------------------------
    Observation: x CAN NOT mutate here because ownership still belongs to y
    ------------------------------------------------------------------
    */
    // x = 222;  // -> WILL NOT WORK

    /*
    ##################################################################
    STEP 3 - RETURN OWNERSHIP => END of borrowing scope

    last use of y
    x gains ownership back
    y loses ownership
    ##################################################################
    */
    let _k: &i32 = &y;

    /*
    ------------------------------------------------------------------
    Observation: x can mutate after borrowing ends
    ------------------------------------------------------------------
    */
    x = 333;

    // ### IGNORE ###
    // use variable to prevent compiler from complaining after mutation
    _nul = x;
}
