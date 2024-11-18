/*
smart pointers - recursive type - cyclic size

Sample raises compilation error due to the fact
that Some refers to itself which leads to infinite size
undeterminable by the compilator for stack allocation.
*/

#[allow(dead_code)]
#[derive(Debug)]
enum Some {
    Foo,
    Bar(Some),
}

fn main() {
    let x = Some::Bar(Some::Bar(Some::Foo));

    println!("{:?}", x);
}
