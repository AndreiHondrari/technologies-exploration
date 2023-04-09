/*
common traits - options - basic functionality
*/


fn main() {
    // functionality for nothing
    println!("\nNothing");

    let mut potential_value: Option<u16> = None;

    let mut is_none: bool = potential_value.is_none();
    println!("is_none:\t{:?}", is_none);

    let mut is_some: bool = potential_value.is_some();
    println!("is_some:\t{:?}", is_some);

    let mut val_ref: Option<&u16> = potential_value.as_ref();
    println!("val_ref:\t{:?}", val_ref);

    // functionality for something
    println!("\nSomething");

    potential_value = Some(123);

    is_none = potential_value.is_none();
    println!("is_none:\t{:?}", is_none);

    is_some = potential_value.is_some();
    println!("is_some:\t{:?}", is_some);

    val_ref = potential_value.as_ref();
    println!("val_ref:\t{:?}", val_ref);
}
