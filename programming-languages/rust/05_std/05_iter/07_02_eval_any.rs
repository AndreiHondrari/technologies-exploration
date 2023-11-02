/*
Iterations - Evaluation - Any
*/

fn main() {
    let values: Vec<u16> = vec![11, 22, 33];

    let result_1: bool = values.iter().any(|x: &u16| *x == 999);
    println!("* == 999 ? : {:?}", result_1);

    let result_2: bool = values.iter().any(|x: &u16| *x == 22);
    println!("* ==  22 ? : {:?}", result_2);
}
