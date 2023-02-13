/*
Generics - type inferring

It is possible to avoid declaring the
generic type to be used by the function,
and instead have the compiler determine
the type by itself, based on the type of the
argument.
*/

fn do_some<T>(x: T) -> T {
    x
}

fn main() {
    let a: u8 = 11;
    let b: i16 = 22;

    let k = do_some(a);
    let p = do_some(b);

    println!("{k}, {p}")
}
