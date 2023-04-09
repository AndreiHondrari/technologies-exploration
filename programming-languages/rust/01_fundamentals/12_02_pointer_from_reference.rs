/*
Structs - pointer from reference

If you have a reference and you want to
initialize a pointer with the address it refers to
you can't get the address by writing `&identifier`,
instead you have to dereference so that we work with
the original memory area.

`&*identifier` and `&(*identifier)` work the same way.
*/


fn main() {

    let x: u16 = 123;

    let y: &u16 = &x;

    let p1: *const u16 = &*y;
    let p2: *const u16 = &(*y);
    // let p3: *const u16 = &y;  // WILL NOT WORK

    unsafe {
        println!("x addr \t{:?}", &x as *const u16);
        println!("p1 \t{:?}", &x as *const u16);
        println!("p2 \t{:?}", &x as *const u16);

        println!("*p1 \t{:?}", *p1);
        println!("*p2 \t{:?}", *p2);
    }
}
