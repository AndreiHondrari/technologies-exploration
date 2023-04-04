/*
smart pointers - recursive type
*/

#[derive(Debug)]
enum Some {
    Foo,
    Bar(Box<Some>)
}

fn main() {
    let x = Some::Bar(
        Box::new(Some::Bar(
            Box::new(Some::Foo)
        ))
    );

    println!("{:?}", x);
}
