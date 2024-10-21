/*
Enums - basic definition
*/


fn main() {

    #[derive(Debug)]
    enum SomeKind {
        POTATO,
        TOMATO
    }

    let mut x = SomeKind::POTATO;
    println!("{:?}", x);
    x = SomeKind::TOMATO;
    println!("{:?}", x);
}
