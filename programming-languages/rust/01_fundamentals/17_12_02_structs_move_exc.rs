/*
Non primitives move - exception exhibit
*/

#[derive(Debug)]
#[allow(dead_code)]
struct Foo {
    x: u16
}

fn main() {
    let original = Foo {x: 111};
    println!("original      {:?}", original);
    
    let new_thing = original;
    println!("new thing     {:?}", new_thing);
    
    // !!! 'original' no longer usable at this point
    let _other_new_thing = original;  // <-- WILL NOT COMPILE
}