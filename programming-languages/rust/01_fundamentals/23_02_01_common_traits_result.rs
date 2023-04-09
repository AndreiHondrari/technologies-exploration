/*
common traits - results
*/


fn main() {
    // NOTICE: Result<T, U>
    // where T for Ok<T>
    // where U for Err<U>
    let mut potential_value: Result<u16, u16> = Ok(123);
    println!("{:?}", potential_value);

    potential_value = Err(999);
    println!("{:?}", potential_value);
}
