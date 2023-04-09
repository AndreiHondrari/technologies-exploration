/*
common traits - options

the std::option::Option is part of the prelude
*/


fn main() {
    // nothing
    let mut potential_value: Option<u16> = None;

    println!("{:?}", potential_value);

    // something
    // NOTICE: the value passed with some is of the type passed to Option
    potential_value = Some(123);

    println!("{:?}", potential_value);
}
