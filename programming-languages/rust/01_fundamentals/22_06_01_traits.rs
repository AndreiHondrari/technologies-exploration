/*
generics - traits
*/


// declare some structs
struct Foo {
    x: u8
}

struct Bar {
    y: i32
}

// declare trait - common behaviour interface
trait Some {
    fn do_some(&self) -> u32;
}

// implement behaviour for structs
impl Some for Foo {
    fn do_some(&self) -> u32 {
        println!("Foo | do_some");
        self.x as u32
    }
}

impl Some for Bar {
    fn do_some(&self) -> u32 {
        println!("Bar | do_some");
        self.y as u32
    }
}


fn main() {
    let s1 = Foo {x: 11};
    let s2 = Bar {y: 22};

    let k: u32 = s1.do_some();
    let p: u32 = s2.do_some();

    println!("{:?}, {:?}", k, p);
}
