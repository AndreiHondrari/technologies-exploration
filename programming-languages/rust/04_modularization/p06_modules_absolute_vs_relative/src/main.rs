mod foo {
    pub mod bar {
        pub fn do_some() {
            println!("doing some ...");
        }
    }
}

fn main() {
    foo::bar::do_some(); // relative
    crate::foo::bar::do_some(); //absolute
}
