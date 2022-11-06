/*
References

NOTICE that here the reference variable itself is mutable,
and it is not the reference it is pointing to that is mutable.
*/


fn main() {
    let mut a: i32 = 111;
    let mut b: i32 = 222;

    let mut x: &i32 = &a;
    println!("#1 X: {}", x);

    x = &b;
    println!("#2 X: {}", x);

    // mutate them so that the compiler does not complain
    a = 333;
    b = 444;

    // use them so that the compiler does not complain
    let mut _nul = a;
    _nul = b;
}
