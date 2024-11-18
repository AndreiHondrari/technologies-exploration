/*
smart pointers - recursive type
*/

#[allow(dead_code)]
#[derive(Debug)]
enum Some {
    Foo,
    Bar(Box<Some>),
}

fn main() {
    let x = Some::Bar(Box::new(Some::Bar(Box::new(Some::Foo))));

    println!("{:?}", x);
}
