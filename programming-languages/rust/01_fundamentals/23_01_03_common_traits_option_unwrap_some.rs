/*
common traits - options - unwrapping
*/


fn main() {
    let potential_value: Option<u16> = Some(123);
    let value: u16 = potential_value.unwrap();
    println!("{:?}", value);
}
