/*
Iterations - Evaluation - Sum
*/

fn main() {
    let values: Vec<u16> = vec![11, 22, 33];

    let result: u16 = values.iter().sum();
    println!("sum: {:?}", result);
}
