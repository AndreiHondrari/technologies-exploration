fn main() {
    let mut v1: Vec<u16> = Vec::new();

    v1.push(11);
    v1.push(22);
    v1.push(33);
    v1.push(44);

    let v1 = v1;

    for x in v1.iter() {
        println!("{x}");
    }
}
