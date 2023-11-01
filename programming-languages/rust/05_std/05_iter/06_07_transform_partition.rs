/*
Iterations - Transform - Partition

Splits the collection into two
based on the boolean result of the predicate function.
*/

fn main() {
    let values: Vec<u16> = (1..20 + 1).into_iter().collect();

    let result: (Vec<u16>, Vec<u16>) = values.into_iter().partition(|&x: &u16| x <= 10);

    let (first_half, second_half): (Vec<u16>, Vec<u16>) = result;

    println!("first half:   {:?}", first_half);
    println!("second half:  {:?}", second_half);
}
