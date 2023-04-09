/*
common traits - equivalence - PartialEq vs Eq
*/

// partial equivalence - unrestricted
struct Foo {
    _x: u16
}

impl PartialEq for Foo {
    fn eq(&self, other: &Self) -> bool {
        self._x == other._x
    }
}

// partial equivalence - restricted
struct Bar {
    _y: u16
}

impl PartialEq for Bar {
    fn eq(&self, other: &Self) -> bool {
        // deliberately checking
        // if we refer to the same object
        // by comparing memory addresses
        let addr1: *const Self = &*self;
        let addr2: *const Self = &*other;

        if addr1 == addr2 {
            return false;
        }

        // the usual evaluation for different instances
        self._y == other._y
    }
}

// full equivalence
struct Kek {
    _p: u32
}

impl PartialEq for Kek {
    fn eq(&self, other: &Self) -> bool {
        self._p == other._p
    }
}

// just a marker
// it doesn't add extra functionality or data
// exists simply for trait bounding checks
impl Eq for Kek {}

fn main() {
    println!("PartialEq unrestricted");
    let f1 = Foo {_x: 11};
    let f2 = Foo {_x: 11};
    let f3 = Foo {_x: 22};

    println!("x == x \t{:?}", f1 == f1);
    println!("x == y \t{:?}", f1 == f2);
    println!("x == z \t{:?}", f1 == f3);

    println!("\nPartialEq restricted");
    let b1 = Bar {_y: 11};
    let b2 = Bar {_y: 11};
    let b3 = Bar {_y: 22};

    println!("x == x \t{:?}", b1 == b1);
    println!("x == y \t{:?}", b1 == b2);
    println!("x == z \t{:?}", b1 == b3);

}
