/*
common traits - results - unwrap error - compilation error
*/


fn main() {
    // Notice: different T and U for consistency
    let potential_value: Result<u32, u8> = Err(77);

    // Will not compiled because Err can not be unwrapped
    let value: u32 = potential_value.unwrap();
    println!("{:?}", value);
}
