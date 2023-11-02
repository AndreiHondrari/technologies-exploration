/*
Iterations - Evaluation - Find
*/

fn main() {
    let values: Vec<u16> = (1..100).collect();

    let result = values.iter().find(|&x: &&u16| *x == 50);

    match result {
        Some(value) => {
            println!("{}", value);
        }

        None => {
            println!("Value not found",);
        }
    }
}
