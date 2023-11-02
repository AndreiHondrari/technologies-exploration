/*
Iterations - Evaluation - Max
*/

fn main() {
    let values: Vec<u16> = vec![11, 22, 33, 44, 55];

    let result = values.iter().max();
    println!("{:?}", result);
}
