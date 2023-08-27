mod foo {
    // declare a function at this level
    fn do_some() {
        println!("doing some ...");
    }

    // delare a module at this level
    mod kek {
        pub fn do_other() {
            println!("doing other ...");
        }
    }

    // declare out public module
    pub mod bar {
        pub fn do_bar() {
            // use the functions declared in the parent module
            super::do_some();
            super::kek::do_other();
        }
    }
}

fn main() {
    // use the public container
    foo::bar::do_bar();
}
