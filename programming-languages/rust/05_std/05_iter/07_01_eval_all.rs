/*
Iterations - Evaluation - All
*/

fn main() {
    let values: Vec<u16> = vec![1, 10, 100];

    let result_1: bool = values.iter().all(|x: &u16| *x < 9_999);
    println!("* < 9999 ? : {:?}", result_1);

    let result_2: bool = values.iter().all(|x: &u16| *x == 100);
    println!("* == 100 ? : {:?}", result_2);
}
