/*
common traits - results - unwrap or passed default
*/


fn main() {
    // unwrapping Ok -> use Ok value
    // Notice: different T and U for consistency
    let mut potential_value: Result<u32, u8> = Ok(111);
    let mut value: u32 = potential_value.unwrap_or(222);
    println!("{:?}", value);

    // unwrapping Err -> use passed default
    potential_value = Err(77);
    value = potential_value.unwrap_or(444);
    println!("{:?}", value);
}
