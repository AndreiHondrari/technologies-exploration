/*
 
*/

#[derive(Debug)]
#[allow(dead_code)]
struct Foo {
    x: u16
}

fn main() {
    let original = Foo {x: 111};
    println!("original      {:?}", original);
    
    // move original into new_thing
    let new_thing = original;
    println!("newe thing    {:?}", new_thing);
    
    // !!! 'original' no longer usable at this point
    
    
}