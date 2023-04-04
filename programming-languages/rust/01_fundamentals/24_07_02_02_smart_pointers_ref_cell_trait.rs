/*
Smart pointers - RefCell - inner mutability with fake implementation

Let's assume we want to provide some implementation
with a reference to another immplementation that has the sole purpose
of tracking it's own utilization within the main implementation,
but without sacrificing immutability of the main implementation,
or without having to change the original signature by having
to declare the self a mutable reference.

RefCell grants us inner mutability within the given limitations. 
*/

use std::cell::RefCell;
use std::cell::RefMut;
use std::cell::Ref;

/*
Define the common interface
to be used by concrete implementations
as well as by fake implementations
(e.g. for mocking purposes).
*/
trait DoSome {
    fn do_some(&self);
}

/*
Define the main structure and its functionality.
This structure depends on the interface that can be
fakeable, with concealed inner mutability.
*/
#[derive(Debug)]
struct Foo<'a, T> {
    sub_foo: &'a T
}

impl<'a, T> Foo<'a, T>
where
    T: DoSome
{
    fn do_foo(&self) {
        self.sub_foo.do_some();
    }
}

/*
Define the fake implementation with inner mutability.

We want 'x' attribute to have inner mutability
WITHOUT having to change the signature of do_some
to accustom mutable self reference.

RefCell grants us this inner_mutability
(instead of using directly the desired type)
*/
#[derive(Debug)]
struct FakeSome {
    // normally we want this to be u32
    // but because we want inner_mutability
    // we wrap it in a RefCell smart pointer
    x: RefCell<u32>
}

impl DoSome for FakeSome {
    fn do_some(&self) {
        // Notice that we borrow a mutable
        // variant of self.x without having to declare
        // self a mutable reference which is normally
        // required by the compiler
        let mut inner_x: RefMut<u32> = self.x.borrow_mut();
        *inner_x = 777;
    }
}

fn main() {
    // instantiate the fake implementation
    let fake_some = FakeSome{x: RefCell::new(123)};

    // instantiate the main structure
    // NOTICE: it is not declared mutable
    let foo: Foo<FakeSome> = Foo {sub_foo: &fake_some};

    // check the value before using the main functionality
    let before_x: Ref<u32> = fake_some.x.borrow();
    println!("BEFORE\t{:?}", before_x);
    // we have to drop the reference
    // because it does not drop automatically
    // (it is characteristic to RefCell)
    drop(before_x);

    // use the main functionality
    // that sub-utilizes the fake implementation
    // with inner mutability
    foo.do_foo();

    // check the value again
    // NOTICE: the value CHANGED even though
    // the main instance was not declared mutable
    let after_x: Ref<u32> = fake_some.x.borrow();
    println!("AFTER\t{:?}", *after_x);
    // no need to drop the borrow here anymore
    // because the scope drops it for us
}
