/*
common traits - ordering - partial - functionality
*/


#[derive(PartialEq, PartialOrd, Debug)]
struct Kek {
    _p: u16
}

fn main() {
    let k1 = Kek {_p: 11};
    let k2 = Kek {_p: 11};
    let k3 = Kek {_p: 22};

    println!("k1 {:?}", k1);
    println!("k1 {:?}", k2);
    println!("k1 {:?}", k3);

    println!("{}", k1.lt(&k3));
    println!("{}", k1.le(&k2));
    println!("{}", k3.gt(&k2));
    println!("{}", k2.ge(&k1));
}
