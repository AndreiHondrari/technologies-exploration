/*
Vectors - properties
*/

fn main() {
    let mut v1: Vec<u16> = vec![11, 22, 33];

    println!("before extend     {:?}", v1);

    println!("...extend");
    v1.extend([77, 88, 99]);

    println!("after extend      {:?}", v1);
}
