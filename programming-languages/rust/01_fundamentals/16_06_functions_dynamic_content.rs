/*
Functions

Functions can't use variables outside their scope
*/



fn main() {
    let x = 123;

    fn my_func() {
        let _y = x;  // will throw error
    }

}
