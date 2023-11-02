/*
Iterations - Evaluation - Greater than or Equal
*/

fn check_ge(first: &Vec<u16>, second: &Vec<u16>) {
    let result: bool = first.iter().ge(second.iter());
    println!(
        "{:<7}ge {:<7}=> {:?}",
        format!("{:?}", first),
        format!("{:?}", second),
        result
    );
}

fn main() {
    let v1: Vec<u16> = vec![1, 2];
    let v2: Vec<u16> = vec![1];
    let v3: Vec<u16> = vec![1, 3];

    check_ge(&v1, &v1);
    check_ge(&v1, &v2);
    check_ge(&v2, &v1);
    check_ge(&v1, &v3);
    check_ge(&v3, &v1);
}
