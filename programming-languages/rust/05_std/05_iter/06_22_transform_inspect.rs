/*
Iterations - Transform - TODO
*/

fn hprint() {
    println!("{}", "-".repeat(50));
}

macro_rules! head_print {
    ($message:expr) => {
        println!("\n{}", $message);
        hprint();
    };
}

fn main() {
    type ValuesIterator<'a> = std::slice::Iter<'a, u16>;

    let values: Vec<u16> = vec![0, 1, 2, 3, 4];

    println!("original:     {:?}", values);

    head_print!("flow");
    let values_iterator: ValuesIterator = values.iter();

    // inspect receives a reference to the &u16 reference, so &&u16
    let inspect_1 = values_iterator.inspect(|&x: &&u16| print!("{:?} -> ", *x));

    // map receives the original reference (&u16)
    // map dereferences value and computes an u16 (!important),
    // value which gets passed further to the next iteration stage
    let mapped_1 = inspect_1.map(|&x: &u16| x + 1);

    // inspect receives a reference to the value from the previous stage (map), so &u16
    let inspect_2 = mapped_1.inspect(|&x: &u16| print!("{:?} -> ", x));

    // map receives the computed value from the previous map stage, so u16
    let mapped_2 = inspect_2.map(|x: u16| x * 11);

    // finally use the end result
    mapped_2.for_each(|x: u16| println!("{:?}", x));

    /*
    NOTICE (!important) the difference between for_each and inspect.

    for_each receives the final value (unreferenced and moved) to consume as
        as the last stage in an iteration stages chain.

    inspect only receives references to values that are passed between iteration stages.
        Can be used intercalated between stages withou affecting them.
    */
}
