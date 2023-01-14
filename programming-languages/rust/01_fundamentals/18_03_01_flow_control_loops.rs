/*
Control flow - loops

Continuously running loops that can be stopped explicitly
*/


fn main() {

    let mut i = 0;

    loop {
        if i >= 5 { break };
        println!("value {i}");
        i += 1;
    }
}
