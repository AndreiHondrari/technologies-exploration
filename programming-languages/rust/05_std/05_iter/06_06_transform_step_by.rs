/*
Iterations - Transform - StepBy
*/

use std::iter::StepBy;
use std::slice::Iter;

fn main() {
    let values: Vec<u16> = (0..50 + 1).collect();

    let values_iterator = values.iter();

    let stepper_iterator: StepBy<Iter<'_, u16>> = values_iterator.step_by(10);

    for x in stepper_iterator {
        println!("{x}");
    }
}
