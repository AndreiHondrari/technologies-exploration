/*
lifetime - multiple ref params - COMPILATION ERROR

When there are multiple ref params then
the compiler will complain because
it does not know how to interpret the
lifetimes of the references
*/

#[allow(unused_variables)]
fn do_some(x: &u16, y: &u16) -> &u16 {
    x
}

fn main() {
    let v = 123u16;

    let r1: &u16 = &v;
    let r2: &u16 = &v;
    let r3: &u16 = do_some(r1, r2);
    println!("{r1}, {r2}, {r3}");
}
