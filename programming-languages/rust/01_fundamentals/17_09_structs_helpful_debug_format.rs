/*
Structs - debug display

Decorate struct with attribute
to enable a default display format
for structs.

Notice the special {:?} format
for debug print.
*/


fn main() {
    #[derive(Debug)] // Notice the attribute
    struct Some {a: u16, b: u16}

    let x = Some {a: 11, b: 22};
    println!("version 1");
    println!("{:?}", x); // Notice the format

    println!("\nversion 2");
    println!("{:#?}", x); // Notice the format

    // ignore
    let _k = (x.a, x.b);

}
