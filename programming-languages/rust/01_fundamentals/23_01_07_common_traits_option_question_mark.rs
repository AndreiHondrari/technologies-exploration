/*
common traits - options - question mark

Equivalent of:

```
let x: Option<u16> = some_function();
if x == None {
    return None
}

return x
```

Notice that '?' unwraps the value or None
*/


fn give_nothing() -> Option<u16> {
    None
}

fn give_something() -> Option<u16> {
    Some(123)
}


fn f1() -> Option<u16> {
    Some(give_nothing()?)
}

fn f2() -> Option<u16> {
    Some(give_something()?)
}


fn main() {
    let mut potential_value: Option<u16> = f1();
    println!("{:?}", potential_value);

    potential_value = f2();
    println!("{:?}", potential_value);
}
