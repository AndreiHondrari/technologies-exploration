/*
generics - methods - return type 
*/
use std::convert::TryFrom;

struct Something {}

impl Something {

    fn do_some<T>(&self) -> T
    where
        T: TryFrom<i32> + Default
    {
        T::try_from(123).unwrap_or_default()
    }
}


fn main() {
    let s1 = Something{};
    let k: u32 = s1.do_some();
    println!("{k}");
}
