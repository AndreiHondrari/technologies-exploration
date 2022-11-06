/*

*/

fn main() {

    // define original variables
    let x = 11;
    let mut y = 22;

    // pointer to the variables
    let px: *const i32 = &x;
    let py: *mut i32 = &mut y;

    println!("# (unsafe) dereference px and py");
    unsafe {
        let mut k = *px;
        println!("{k}");

        k = *py;
        println!("{k}");
    }
}
