/*
Pattern matching - regular values
*/


fn choose(kind: u32) {
    match kind {
        11 => {
            println!("this");
        },

        22 => {
            println!("that");
        },

        // Catch-all has to be present
        // otherwise compiler complains
        // that no all u32 values are used
        _ => ()
    };
}

fn main() {
    choose(11);
    choose(22);
}
