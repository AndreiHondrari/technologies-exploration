/*
Iterator - next
*/

fn main() {
    let v1: Vec<i32> = vec![11, 22, 33, 44, 55, 66];

    let mut v1_iterator: std::slice::Iter<'_, i32> = v1.iter();

    // let mut v;

    println!("before a few steps");
    println!("{}", "-".repeat(50));
    println!("size hint:    {:?}", v1_iterator.size_hint());

    println!("\ndo some steps ...\n");
    v1_iterator.next();
    v1_iterator.next();

    println!("after a few steps");
    println!("{}", "-".repeat(50));
    println!("size hint:    {:?}", v1_iterator.size_hint());
}
