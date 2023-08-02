/*
lifetime - multiple ref params - annotating everything
*/

#[allow(unused_variables)]
fn do_some<'a>(x: &'a u16, y: &'a u16) -> &'a u16 {
    x
}

fn main() {
    let v = 123u16;

    let r1: &u16 = &v;
    let r2: &u16 = &v;
    let r3: &u16 = do_some(r1, r2);
    println!("{r1}, {r2}, {r3}");
}
