/*
common traits - ordering - total

Ord is for PartialOrd as Eq is for PartialEq
Ord is bounded by Eq and PartialOrd, which indirectly means it is bounded by PartialEq
Ord practically represents a comparison relation where all elements can be compared.
It does not prevent you from making mistakes like turning the cmp into
a partial order binary relation.

Usually cmp is implemented to delegate to cmp of a
specific member of the structure, or a combination of those.
*/

use std::cmp::Ordering;

#[derive(PartialEq, Eq, PartialOrd, Debug)]
struct Kek {
    p: u16
}

impl Ord for Kek {
    fn cmp(&self, other: &Self) -> Ordering {
        self.p.cmp(&other.p)
    }
}

fn main() {
    let k1 = Kek {p: 111};
    let k2 = Kek {p: 111};
    let k3 = Kek {p: 222};

    println!("# Compare to itself");
    println!("k1 <= k1 \t{}", k1 <= k1);  // true
    println!("k1 <  k1 \t{}", k1 <  k1);  // false
    println!("k1 >= k1 \t{}", k1 >= k1);  // true
    println!("k1 >  k1 \t{}", k1 >  k1);  // false

    println!("\n# Compare to identical other structure");
    println!("k1 <= k2 \t{}", k1 <= k2);  // true
    println!("k1 <  k2 \t{}", k1 <  k2);  // false
    println!("k1 >= k2 \t{}", k1 >= k2);  // true
    println!("k1 >  k2 \t{}", k1 >  k2);  // false

    println!("\n# Compare to different other structure");
    println!("k1 <= k3 \t{}", k1 <= k3);  // true
    println!("k1 <  k3 \t{}", k1 <  k3);  // true
    println!("k1 >= k3 \t{}", k1 >= k3);  // false
    println!("k1 >  k3 \t{}", k1 >  k3);  // false
    println!("k3 >= k1 \t{}", k3 >= k1);  // true
    println!("k3 >  k1 \t{}", k3 >  k1);  // true
}
