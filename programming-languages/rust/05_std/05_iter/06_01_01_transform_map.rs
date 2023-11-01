/*
Iterations - Transform - Map
*/

use std::iter::Map;
use std::slice::Iter;

fn main() {
    let values: Vec<u16> = vec![11, 22, 33];

    let values_map: Map<Iter<'_, u16>, fn(&u16) -> u16> = values.iter().map(|x| x * 2);

    for x in values_map {
        println!("{x}");
    }
}
