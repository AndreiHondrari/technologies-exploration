/*
Iterations - Evaluation - Partial Cmp
*/

fn hprint() {
    println!("{}", "-".repeat(50));
}

macro_rules! head_print {
    ($message:expr) => {
        println!("\n{}", $message);
        hprint();
    };
}

fn compare(first: &Vec<f32>, second: &Vec<f32>) {
    let result: Option<std::cmp::Ordering> = first.iter().partial_cmp(second.iter());
    println!(
        "{:<10}\tand\t{:<10}\t=> {:?}",
        format!("{:?}", first),
        format!("{:?}", second),
        result
    );
}

fn main() {
    let v1: Vec<f32> = vec![1.0, 2.0];
    let v2: Vec<f32> = vec![1.0];
    let v3: Vec<f32> = vec![1.0, 3.0];
    let v4: Vec<f32> = vec![7.0, f32::NAN];
    let v5: Vec<f32> = vec![8.0, f32::NAN];
    let v6: Vec<f32> = vec![f32::NAN, 9.0];
    let v7: Vec<f32> = vec![f32::NAN, 3.0];

    head_print!("Regular partial compare for typical values");
    compare(&v1, &v1);
    compare(&v1, &v2);
    compare(&v2, &v1);
    compare(&v1, &v3);
    compare(&v3, &v1);

    head_print!("Partial compare with NaN's");
    compare(&v4, &v4);
    compare(&v4, &v5);
    compare(&v5, &v4);
    compare(&v4, &v6);
    compare(&v6, &v4);
    compare(&v6, &v7);
}
