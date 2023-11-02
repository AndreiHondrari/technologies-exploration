/*
Iterations - Evaluation - Cmp
*/

fn compare(first: &Vec<u16>, second: &Vec<u16>) {
    let result: std::cmp::Ordering = first.iter().cmp(second.iter());
    println!("{:?} \t{:?} \t => {:?}", first, second, result);
}

fn main() {
    let v1: Vec<u16> = vec![1, 2];
    let v2: Vec<u16> = vec![1];
    let v3: Vec<u16> = vec![1, 3];

    compare(&v1, &v1);
    compare(&v1, &v2);
    compare(&v2, &v1);
    compare(&v1, &v3);
    compare(&v3, &v1);
}
