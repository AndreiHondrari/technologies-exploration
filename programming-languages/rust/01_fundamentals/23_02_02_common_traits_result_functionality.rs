/*
common traits - results - basic functionality
*/


fn main() {
    // functionality for success
    println!("Success");

    let mut potential_value: Result<u16, u16> = Ok(123);

    let mut is_ok: bool = potential_value.is_ok();
    println!("is_ok\t{:?}", is_ok);

    let mut is_err: bool = potential_value.is_err();
    println!("is_err\t{:?}", is_err);

    // functionality for error
    println!("\nError");

    potential_value = Err(999);

    is_ok = potential_value.is_ok();
    println!("is_ok\t{:?}", is_ok);

    is_err = potential_value.is_err();
    println!("is_err\t{:?}", is_err);
}
