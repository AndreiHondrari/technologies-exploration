/*
Iterations - Evaluation - Position
*/

fn main() {
    let values: Vec<u16> = (0..100).step_by(5).collect();

    let result = values.iter().position(|x: &u16| *x >= 50);

    match result {
        Some(value) => {
            println!("found at index: {}", value);
        }

        None => {
            println!("Value not found",);
        }
    }
}
