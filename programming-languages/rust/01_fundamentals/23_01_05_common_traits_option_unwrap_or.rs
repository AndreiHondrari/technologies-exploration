/*
common traits - options - unwrapping or passed default
*/


fn main() {
    // unwrap a None will use passed default
    let mut potential_value: Option<u16> = None;
    let mut value: u16 = potential_value.unwrap_or(111);
    println!("{:?}", value);  // passed default

    // unwrap a Some will ignore the passed default
    potential_value = Some(222);
    value = potential_value.unwrap_or(333);
    println!("{:?}", value);  // option value
}
