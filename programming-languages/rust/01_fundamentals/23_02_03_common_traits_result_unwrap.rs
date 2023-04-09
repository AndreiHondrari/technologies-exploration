/*
common traits - results - unwrap
*/


fn main() {
    // Notice: different T and U for consistency
    let potential_value: Result<u32, u8> = Ok(123);
    let value: u32 = potential_value.unwrap();
    println!("{:?}", value);
}
