/*
Various ways to print.
*/

fn main() {
    print!("aaa");

    const Y: &'static str = "bbb";
    print!("{}", Y);

    let z: String = String::from("ccc");

    print!("{}", z);
    print!(" ... {z}\n");

    println!("{}, {}", Y, z);
    println!("{}, {}", "ddd", "eee");
}
