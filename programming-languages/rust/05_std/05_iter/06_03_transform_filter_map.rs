/*
Iterations - Transform - Filter Map
*/

use std::iter::{Copied, FilterMap};
use std::slice::Iter;

fn main() {
    type CopiedValues<'a> = Copied<Iter<'a, u16>>;

    let values: Vec<u16> = (0..20).into_iter().collect();

    let values_iterator: CopiedValues = values.iter().copied();

    let filter_mapped_values: FilterMap<CopiedValues, fn(u16) -> Option<u16>> =
        values_iterator.filter_map(|x: u16| if x % 2 == 0 { Some(x * 100) } else { None });

    let result: Vec<u16> = filter_mapped_values.collect();

    println!("{result:?}");
}
