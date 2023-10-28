/*
Iterator - count
*/

fn main() {
    let v1: Vec<i32> = vec![11, 22, 33, 44, 55, 66, 77, 88, 99];

    let mut v1_iterator: std::slice::Iter<'_, i32> = v1.iter();

    let v1_count = v1_iterator.clone().count();
    println!("count before:     {}", v1_count);

    println!("consume a few items from the iterator ...");
    v1_iterator.next();
    v1_iterator.next();
    v1_iterator.next();
    v1_iterator.next();

    let v1_count = v1_iterator.clone().count();
    println!("count after:      {}", v1_count);
}
