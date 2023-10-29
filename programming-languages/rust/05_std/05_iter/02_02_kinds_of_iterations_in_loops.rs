/*
Iterators - kinds of iterations
*/

macro_rules! head_print {
    ($message:expr) => {
        println!("\n{}", $message);
        println!("{}", "-".repeat(50));
    };
}

/*
iteration over references.
loop yields references
*/
fn iterator_on_references(values: [u8; 3]) {
    // each val is a &u8
    for val in &values {
        println!("ref val {}", val);
    }
}

/*
iteration over mutable references.
loop yields mutable references
*/
fn iterator_on_mutable_references(mut values: [u8; 3]) {
    println!("array before mutation:    {:?}", values);

    // each val is a &mut u8
    for val in &mut values {
        *val *= 5;
    }

    println!("array after mutation:     {:?}", values);
}

/*
iteration over values.
loop yields values
*/
fn iterator_on_values(values: [u8; 3]) {
    // each val is a u8
    for val in values {
        println!("val {}", val);
    }
}

fn main() {
    let values: [u8; 3] = [11, 22, 33];
    println!("original array:    {:?}", values);

    head_print!("Iterator on references");
    iterator_on_references(values);

    head_print!("Iterator on mutable references");
    iterator_on_mutable_references(values);

    head_print!("Iterator on values");
    iterator_on_values(values);
}
