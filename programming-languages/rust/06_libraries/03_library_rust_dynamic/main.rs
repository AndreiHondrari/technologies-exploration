#[link(name = "some", kind = "dylib")]
extern "C" {
    fn do_something();
}

fn main() {
    unsafe {
        do_something();
    }
}
