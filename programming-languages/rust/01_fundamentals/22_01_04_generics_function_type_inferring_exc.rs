/*
Generics - type inferring

If you try to mutate a result from a
function that uses generic types
with a value of a different type,
it will not work.
*/

fn do_some<T>(x: T) -> T {
    x
}

fn main() {
    let a: u8 = 11;

    let mut k = do_some(a);
    let _z = k;  // ignore

    let p: i32 = 2222;
    k = p;  // WILL NOT WORK
}
