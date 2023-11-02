/*
Iterations - Evaluation - Count
*/

fn main() {
    let values: Vec<u16> = vec![11, 22, 33, 44, 55, 66, 77, 88, 99, 111];

    let result: usize = values.iter().count();
    println!("counted : {:?}", result);
}
