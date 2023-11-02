/*
Iterations - Evaluation - Max By Key
*/

fn main() {
    let values: Vec<f32> = vec![1.55, 2.42, 3.99, 4.32, 5.71];

    let result = values
        .iter()
        .max_by_key::<u32, fn(&&f32) -> u32>(|&x: &&f32| {
            /*
            Let's absurdly assume we want to compare
            by first 3 fractional digits exclusively.
            */
            let real = *x as u32;
            let fractional: f32 = *x - (real as f32);
            let scaled: u32 = (fractional * 1_000.0) as u32;

            println!("fractional part for {:?} -> {:?}", *x, scaled);

            return scaled;
        });
    println!("\nRESULT: {:?}", result);
}
