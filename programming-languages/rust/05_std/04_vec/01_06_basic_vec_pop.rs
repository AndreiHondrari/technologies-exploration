/*
Vectors - capacity increase

Notice it doubles every time it crosses the limit
*/

fn main() {
    let mut v1: Vec<u16> = vec![11, 22, 33];

    loop {
        let maybe_val: Option<u16> = v1.pop();

        match maybe_val {
            Some(value) => {
                println!("step {}", value);
            }

            None => {
                println!("nothing else");
                break;
            }
        };
    }
}
