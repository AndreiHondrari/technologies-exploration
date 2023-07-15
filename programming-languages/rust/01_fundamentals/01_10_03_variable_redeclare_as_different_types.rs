/*
Redeclare variable as different type
*/

fn main() {
    let x: bool = true;
    println!("A {x}");

    let x: u16 = 111;
    println!("B {x}");

    let x: f32 = 22.22;
    println!("C {x}");

    let x: String = String::from("some string");
    println!("D {x}");
}
