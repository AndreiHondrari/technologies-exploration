/*
Iterations - Evaluation - Fold
*/

fn main() {
    let values: Vec<u32> = vec![3, 20, 100];

    let result: u32 = values.iter().fold(7_000, |acc: u32, x: &u32| *x + acc);
    println!("{:?}", result);
}
