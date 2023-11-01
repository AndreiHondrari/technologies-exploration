/*
Iterations - Transform - Flatten
*/

use std::iter::{Flatten, Map};

fn main() {
    type UltraVectorsIterator<'a> = std::slice::Iter<'a, Vec<u16>>;
    type SubvectorIntoIter<'a> = std::slice::Iter<'a, u16>;
    type MappedVectors<'a> = Map<UltraVectorsIterator<'a>, fn(&Vec<u16>) -> SubvectorIntoIter>;

    let v1: Vec<u16> = vec![11, 22, 33];
    let v2: Vec<u16> = vec![44, 55];

    let ultra_vector: Vec<Vec<u16>> = vec![v1, v2];

    let ultra_vector_iterator: UltraVectorsIterator = ultra_vector.iter();

    let mapper_iterator: MappedVectors =
        ultra_vector_iterator.map(|subvect: &Vec<u16>| subvect.into_iter());

    let flatten_iterator: Flatten<MappedVectors> = mapper_iterator.flatten();

    let result: Vec<&u16> = flatten_iterator.collect();

    println!("{:?}", result);
}
