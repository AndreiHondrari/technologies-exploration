/*
common traits - ordering - total - functionality
*/

#[derive(PartialEq, Eq, PartialOrd, Ord, Debug, Clone, Copy)]
struct Kek {
    p: u16
}

fn main() {
    let k1 = Kek {p: 111};
    let k2 = Kek {p: 222};

    println!("# Min/max");
    println!("k1.max(&k1) \t{:?}", k1.max(k1));
    println!("k1.max(&k2) \t{:?}", k1.max(k2));
    println!("k1.min(&k2) \t{:?}", k1.min(k2));

    println!("\n# Clamping");
    let kmin = Kek {p: 100};
    let kmax = Kek {p: 200};

    let k3 = Kek {p: 90};
    let k4 = Kek {p: 150};
    let k5 = Kek {p: 201};

    println!("k3.clamp(kmin, kmax) \t{:?}", k3.clamp(kmin, kmax));
    println!("k4.clamp(kmin, kmax) \t{:?}", k4.clamp(kmin, kmax));
    println!("k5.clamp(kmin, kmax) \t{:?}", k5.clamp(kmin, kmax));
}
