/*
common traits - options - unwrapping nothing - panic error
*/

fn main() {
    let potential_value: Option<u16> = None;

    // Will panic because None can not be unwrapped
    let _value: u16 = potential_value.unwrap();
}
