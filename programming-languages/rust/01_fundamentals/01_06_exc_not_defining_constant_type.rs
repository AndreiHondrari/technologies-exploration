/*
Const require an explicit type.
Type can't be implied for constants as
they are baked in the final binary as
a static value.
*/

fn main() {
    const x = 11;
    println!("{x}");
}
