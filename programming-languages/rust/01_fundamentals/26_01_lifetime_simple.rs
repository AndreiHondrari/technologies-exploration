/*
lifetime - no lifetime for single parameter refs

notice that x and return value of the function
do not require lifetime annotation
*/

fn do_some(x: &u16) -> &u16 {
    x // NOTICE IT SIMPLY RETURNS THE REFERENCE
}

fn main() {
    let v = 123u16;

    let r1: &u16 = &v;
    let r2: &u16 = do_some(r1);
    println!("{r1}, {r2}");
}
