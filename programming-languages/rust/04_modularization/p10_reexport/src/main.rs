mod foo;

fn main() {
    println!("Hello, world!");
    foo::kek::do_kek(); // 'kek' is re-exported by foo
}
