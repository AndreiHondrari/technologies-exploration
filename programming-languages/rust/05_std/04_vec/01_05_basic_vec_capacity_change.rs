/*
Vectors - capacity increase

Notice it doubles every time it crosses the limit
*/

fn main() {
    let mut v1: Vec<u16> = vec![];

    let mut last_capacity: usize = v1.capacity();
    let mut new_capacity: usize;

    for i in 1..1025 + 1 {
        v1.push(0);
        new_capacity = v1.capacity();

        if new_capacity > last_capacity {
            println!(
                "[{}] new max capacity: {} at len {}",
                i,
                new_capacity,
                v1.len()
            );
            last_capacity = new_capacity;
        }
    }
}
