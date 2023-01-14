/*
Control flow - assign from if

Conditional assignment
*/


fn main() {

    let x = 10;

    let a = if x > 0 { 11 } else { 22 };
    let b = if x == 20 { 33 } else if x == 15 { 44 } else { 55 };

    println!("A {a} B {b}");
}
