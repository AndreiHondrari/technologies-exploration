
extern {
    fn do_something();
}

fn main() {

    unsafe {
        do_something();
    }
}
