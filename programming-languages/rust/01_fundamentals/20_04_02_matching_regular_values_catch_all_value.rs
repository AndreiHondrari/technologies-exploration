/*
Pattern matching - regular values
use unmatched value
*/


fn choose(kind: u32) {
    match kind {
        11 => {
            println!("kaboom");
        },

        other => {
            println!("OTHER {other}");
        }
    };
}

fn main() {
    choose(11);
    choose(22);
    choose(33);
}
