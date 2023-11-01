/*
Iterations - Transform - Flat Map
*/

use std::iter::FlatMap;

fn main() {
    type UltraVectorsIterator<'a> = std::slice::Iter<'a, Vec<u16>>;
    type SubvectorIntoIter<'a> = std::slice::Iter<'a, u16>;

    let v1: Vec<u16> = vec![11, 22, 33];
    let v2: Vec<u16> = vec![44, 55];

    let ultra_vector: Vec<Vec<u16>> = vec![v1, v2];

    let ultra_vector_iterator: UltraVectorsIterator = ultra_vector.iter();

    let flat_map_iterator: FlatMap<
        UltraVectorsIterator,
        SubvectorIntoIter,
        fn(&Vec<u16>) -> SubvectorIntoIter,
    > = ultra_vector_iterator.flat_map(|subvect: &Vec<u16>| subvect.into_iter());

    let result: Vec<&u16> = flat_map_iterator.collect();

    println!("{:?}", result);
}
