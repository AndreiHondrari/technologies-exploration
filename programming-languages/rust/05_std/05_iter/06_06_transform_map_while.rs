/*
Iterations - Transform - Map While

Iteration stops when the predicate returns the first None
*/

fn main() {
    type ValuesIterator = std::vec::IntoIter<u16>;

    let values: Vec<u16> = vec![5, 2, 4, 2, 1, 0, 3, 7, 4, 5, 1];

    let values_iterator: ValuesIterator = values.into_iter();

    // iteration interrupts at value 0
    let values_map_while_iterator =
        values_iterator.map_while(|x| if x > 0 { Some(x) } else { None });

    let result: Vec<u16> = values_map_while_iterator.collect();

    println!("result: {:?}", result);
}
