/*
Iterations - Evaluation - Product
*/

fn main() {
    let values: Vec<u16> = vec![1, 20, 200];

    let result: u16 = values.iter().product();
    println!("multiplied to: {:?}", result);
}
