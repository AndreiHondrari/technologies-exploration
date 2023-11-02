/*
Iterations - Evaluation - Find map
*/

fn main() {
    let values: Vec<u16> = (0..100).step_by(5).collect();

    let result = values
        .iter()
        .find_map(|&x: &u16| if x == 50 { Some(123) } else { None });

    match result {
        Some(value) => {
            println!("{}", value);
        }

        None => {
            println!("Value not found",);
        }
    }
}
