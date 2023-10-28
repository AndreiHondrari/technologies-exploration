/*
Iterator - peek
*/

fn main() {
    let v1: Vec<i32> = vec![11, 22];

    let mut v1_iterator: std::slice::Iter<'_, i32> = v1.iter();

    let mut v1_peekable = v1_iterator.clone().peekable();

    let next_value = v1_peekable.peek();
    println!("first peek:    {:?}", next_value);

    println!("consume the iterator ...");
    loop {
        let value = v1_iterator.next();

        if value == None {
            break;
        }
    }

    v1_peekable = v1_iterator.clone().peekable();
    let next_value = v1_peekable.peek();
    println!("second peek:   {:?}", next_value);
}
