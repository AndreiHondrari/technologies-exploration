// create the nested mod structure
mod some_mod {
    pub mod child_mod {
        pub fn do_some() {
            println!("doing some ...");
        }
    }
}

// import the submodule from the mod tree
use some_mod::child_mod;

fn main() {
    child_mod::do_some();
}
