/*
common traits - options - unwrapping or implicit default
*/


fn main() {
    // unwrap a None will use implicit default
    let mut potential_value: Option<u16> = None;
    let mut value: u16 = potential_value.unwrap_or_default();
    println!("{:?}", value);  // implicit default

    // unwrap a Some will give option value
    potential_value = Some(123);
    value = potential_value.unwrap_or_default();
    println!("{:?}", value);  // option value
}
