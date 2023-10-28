/*
Iterator - next
*/

fn main() {
    let v1: Vec<i32> = vec![11, 22, 33];

    let mut v1_iterator: std::slice::Iter<'_, i32> = v1.iter();

    let mut val;

    val = v1_iterator.next();
    println!("{:?}", val);
    val = v1_iterator.next();
    println!("{:?}", val);
    val = v1_iterator.next();
    println!("{:?}", val);
    val = v1_iterator.next();
    println!("{:?}", val);
}
