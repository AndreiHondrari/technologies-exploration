/*
Generics - function generic type

Functions can declare generic types for
arguments and for returning values.

When calling the function you have the ability
of annotating the function with the type
that will be used for that specific call.
*/

fn do_some<T>(x: T) -> T {
    x
}

fn main() {
    let _a: u8 = 10;
    let _b: i16 = 1;

    let _k = do_some::<u8>(_a);

    // WILL NOT WORK
    // let _m = do_some::<u8>(_b);
}
