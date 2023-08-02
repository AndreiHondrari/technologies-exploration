/*
lifetime - multiple ref params - single annotation

If we annotate at least one param with a lifetime
then compilation succeeds
*/

#[allow(unused_variables)]
fn do_this<'a>(x: &'a u16, y: &u16) -> &'a u16 {
    x
}

#[allow(unused_variables)]
fn do_that<'a>(x: &u16, y: &'a u16) -> &'a u16 {
    y
}

fn main() {
    let v = 123u16;

    let r1: &u16 = &v;
    let r2: &u16 = &v;
    let r3: &u16 = do_this(r1, r2);
    let r4: &u16 = do_that(r1, r2);
    println!("{r1}, {r2}, {r3}, {r4}");
}
