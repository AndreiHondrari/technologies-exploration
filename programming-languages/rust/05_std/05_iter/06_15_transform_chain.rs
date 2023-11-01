/*
Iterations - Transform - Chain
*/

fn main() {
    let v1: Vec<u16> = vec![11, 22, 33];
    let v2: Vec<u16> = vec![999, 777, 555];

    let v1_iterator = v1.iter();
    let v2_iterator = v2.iter();

    let chain_iterator = v1_iterator.chain(v2_iterator);

    let result: Vec<&u16> = chain_iterator.collect();

    println!("{:?}", result);
}
