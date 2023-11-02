/*
Iterations - Evaluation - R-Position
*/

// use std::iter::FromIterator;
use std::iter::{Rev, StepBy};
use std::ops::Range;

fn main() {
    let r0 = 0..100 + 1;
    let r1: StepBy<Range<u16>> = r0.clone().step_by(5);
    let r2: StepBy<Rev<Range<u16>>> = r0.clone().rev().step_by(3);
    let values: Vec<u16> = r1.into_iter().chain(r2.into_iter()).collect();

    let result = values.iter().rposition(|&x: &u16| x >= 50);

    match result {
        Some(value) => {
            println!("found at index: {}", value);
        }

        None => {
            println!("Value not found",);
        }
    }
}
