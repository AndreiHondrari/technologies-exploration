/*
Tuples are fixed data structures that
can keep a mixed collection of values.
(e.g. strings with numbers).

These are good for returning
multiple values from functions.

! Tuples can not be iterated !

It is also not possible to use
a dynamic index for the tuple.

Example:
```
let t1 = (123, "bla");

for x in 0..2 {
    print!("{}", t1.x);  // NOT POSSIBLE
}
```

*/

fn main() {
    let var1 = ("hello", 123, 'x', 23.45);

    println!("{}", var1.0);
    println!("{}", var1.1);
    println!("{}", var1.2);
}
