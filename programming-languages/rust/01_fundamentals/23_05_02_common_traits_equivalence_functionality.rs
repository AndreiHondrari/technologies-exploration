/*
common traits - equivalence - PartialEq functionality
*/

// full equivalence
struct Kek {
    _p: u32
}

impl PartialEq for Kek {
    fn eq(&self, other: &Self) -> bool {
        self._p == other._p
    }
}

impl Eq for Kek {}

fn main() {
    let k1 = Kek {_p: 11};
    let k2 = Kek {_p: 11};
    let k3 = Kek {_p: 22};

    println!("eq");
    println!("k1.eq(&k1) \t{}", k1.eq(&k1));
    println!("k1.eq(&k2) \t{}", k1.eq(&k2));
    println!("k1.eq(&k3) \t{}", k1.eq(&k3));

    println!("\nne");
    println!("k1.ne(&k1) \t{}", k1.ne(&k1));
    println!("k1.ne(&k2) \t{}", k1.ne(&k2));
    println!("k1.ne(&k3) \t{}", k1.ne(&k3));
}
