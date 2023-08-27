mod some_mod;

use some_mod::do_something;

fn main() {
    println!("Hello, world!");

    // use function under package
    some_mod::do_something(String::from("AAA"));

    // use function imported from package specifically
    do_something(String::from("BBB"));
}
