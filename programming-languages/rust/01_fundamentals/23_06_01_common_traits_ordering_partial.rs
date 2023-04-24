/*
common traits - ordering - partial

A partial order is a binary relation on a set
where not all values of the set can be ordered.

As an example we will define a magical value that
can be equal only to itself.

That means that:
- other values cannot equal the magical values
- other values can be equal to themselves

As a consequence, a structure holding such a value
is not worthy of marked with the `Eq` trait,
as it does not satisfy the conditions
for total equality.

As such, the ordering of such a structure
can be only partial, since not all
values are comparable to each other.
*/

use std::cmp::Ordering;


#[derive(Debug)]
struct SpecialThing {
    x: u16
}

/*
Let's define our magic value
used to create special conditions
for the equality and order binary relations
*/
const MAGIC_VALUE: u16 = 111;


/*
Let's define a partial equality relation
where the two structures are equal if and only if
both of their internal values are the magic value
*/
impl PartialEq for SpecialThing {
    fn eq(&self, other: &SpecialThing) -> bool {
        self.x == MAGIC_VALUE && other.x == MAGIC_VALUE
    }
}

/*
Let's define a partial order relation
where the structs can be comparable if and only if
their internal values are not the magic value
*/
impl PartialOrd for SpecialThing {
    // Notice the function returns an Option and not a boolean
    // that means that lt, gt, le, ge
    // will compare with None as well when evaluating
    // the relation
    fn partial_cmp(&self, other: &SpecialThing) -> Option<Ordering> {
        if self.x == MAGIC_VALUE || other.x == MAGIC_VALUE {
            return None
        }

        return self.x.partial_cmp(&other.x);
    }
}

fn main() {

    // magical structures
    let v1 = SpecialThing{x: 111};
    let v2 = SpecialThing{x: 111};

    // non-magical structures
    let v3 = SpecialThing{x: 222};

    let v4 = SpecialThing{x: 333};
    let v5 = SpecialThing{x: 333};

    /*
    Partial equality evaluation
    */
    println!("# Equality checks\n");

    // magic value equal to itself
    // for same structure
    println!("v1 111 == v1 111 \t{:?}", v1 == v1);  // true

    // magic value equal to itself
    // for different structure
    println!("v1 111 == v2 111 \t{:?}", v1 == v2);  // true

    // magic value not equal to a non-magic value
    println!("v1 111 == v3 222 \t{:?}", v1 == v3);  // false

    // non-magic values not equal to themselves no matter what
    println!("v4 333 == v4 333 \t{:?}", v4 == v4);  // false
    println!("v4 333 == v5 333 \t{:?}", v4 == v5);  // false

    /*
    Magical comparisons

    Irregular ordering
    */
    println!("\n# Ordering checks for magic value\n");

    println!("v1 111 <= v1 111 \t{}", v1 <= v1);
    println!("v1 111 <  v1 111 \t{}", v1 < v1);
    println!("v1 111 >= v1 111 \t{}", v1 >= v1);
    println!("v1 111 >  v1 111 \t{}", v1 > v1);

    println!("v1 111 <= v3 222 \t{}", v1 <= v3);
    println!("v1 111 <  v3 222 \t{}", v1 < v3);
    println!("v1 111 >= v3 222 \t{}", v1 >= v3);
    println!("v1 111 >  v3 222 \t{}", v1 > v3);

    /*
    Non-magical comparisons
    Normal ordering
    */
    println!("\n# Ordering checks for non-magic values\n");

    println!("v3 111 <= v4 222 \t{}", v3 <= v4);  // true
    println!("v3 111 <  v4 222 \t{}", v3 < v4);   // true
    println!("v3 111 >= v4 222 \t{}", v3 >= v4);  // false
    println!("v3 111 >  v4 222 \t{}", v3 > v4);   // false
    println!("v4 111 >= v3 222 \t{}", v4 >= v3);  // true
    println!("v4 111 >  v3 222 \t{}", v4 > v3);   // true

}
