/*
Iterations - Evaluation - Min
*/

fn main() {
    let values: Vec<u16> = vec![11, 22, 33, 44, 55];

    let result = values.iter().min();
    println!("{:?}", result);
}
