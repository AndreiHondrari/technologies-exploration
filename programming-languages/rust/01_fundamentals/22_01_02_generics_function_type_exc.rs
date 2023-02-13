/*
Generics - function generic type mismatch

Exception showcasing mismatch between
annotated type and parameter type
*/

fn do_some<T>(x: T) -> T {
    x
}

fn main() {
    let _a: u8 = 10;

    // WILL NOT WORK
    let _m = do_some::<i32>(_a);
}
