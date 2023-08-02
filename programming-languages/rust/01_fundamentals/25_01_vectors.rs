/*
Vectors
*/

fn main() {
    let mut v: Vec<i32> = Vec::new();
    v.push(111);
    v.push(222);
    v.push(333);

    for item in v.iter() {
        println!("{item}");
    }
}
