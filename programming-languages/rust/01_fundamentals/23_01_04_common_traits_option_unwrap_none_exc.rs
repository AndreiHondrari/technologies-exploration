/*
common traits - options - unwrapping nothing - compilation error
*/


fn main() {
    let potential_value: Option<u16> = None;

    // Will not compile because None can not be unwrapped
    let _value: u16 = potential_value.unwrap();
}
