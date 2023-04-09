/*
common traits - results - ok/err as options
*/


fn main() {
    println!("Against Ok");
    // Notice: different T and U for consistency
    let mut potential_value: Result<u32, u8> = Ok(111);

    let mut good_part: Option<u32> = potential_value.ok();
    let mut bad_part: Option<u8> = potential_value.err();
    println!("ok part \t{:?}", good_part);
    println!("err part \t{:?}", bad_part);

    println!("\nAgainst Err");

    potential_value = Err(222);

    good_part = potential_value.ok();
    bad_part = potential_value.err();
    println!("ok part \t{:?}", good_part);
    println!("err part \t{:?}", bad_part);
}
