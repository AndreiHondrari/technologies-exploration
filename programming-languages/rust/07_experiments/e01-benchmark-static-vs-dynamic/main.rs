/*
Whatever
*/

use std::time::Instant;

struct Some;

trait Kek {}

impl Kek for Some {}

fn do_static<T: Kek>(_obj: &T) {}

fn do_dynamic(_obj: &dyn Kek) {}

const ITERATIONS_COUNT: u32 = 1_000_000;

fn main() {
    let obj = Some;

    println!("\t\tTOTAL\t\tAVERAGE");

    // STATIC
    let start = Instant::now();
    for _ in 0..ITERATIONS_COUNT {
        do_static::<Some>(&obj);
    }
    let elapsed_static = start.elapsed();
    let average = elapsed_static / ITERATIONS_COUNT;
    println!("STATIC\t\t{:?}\t{:?}", elapsed_static, average);

    // DYNAMIC

    let start = Instant::now();
    for _ in 0..ITERATIONS_COUNT {
        do_dynamic(&obj);
    }
    let elapsed_dynamic = start.elapsed();
    let average = elapsed_dynamic / ITERATIONS_COUNT;
    println!("DYNAMIC\t\t{:?}\t{:?}", elapsed_dynamic, average);

    println!(
        "\nABSOLUTE DIFFERENCE: {:?}\n",
        elapsed_static.abs_diff(elapsed_dynamic)
    );
}
