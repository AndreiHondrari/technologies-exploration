/*
Iterations - Evaluation - Reduce

The differences from fold() are:
    - the result is an option
    - there is no initial accumulator (only the first element in the collection)
*/

fn main() {
    let values: Vec<u32> = vec![7_000, 3, 20, 100];

    let result: u32 = values
        .iter()
        .copied()
        .reduce(|acc: u32, x: u32| x + acc)
        .unwrap();

    println!("reduced to: {:?}", result);
}
