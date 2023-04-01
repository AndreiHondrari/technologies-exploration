/*
Smart pointers - prequel to RefCell - compilation error due to immutability

Let's assume we want to provide some implementation
with a reference to another immplementation that has the sole purpose
of tracking it's own utilization within the main implementation,
but without sacrificing immutability of the main implementation,
or without having to change the original signature by having
to declare the self a mutable reference.

Normally it is not possible to introduce
mutability of an attribute of a structure
without declaring the owner structure
as mutable.

This sample showcases the compilation error.
*/

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

#[derive(Debug)]
struct FakeSome {
    x: u32
}

impl DoSome for FakeSome {
    // This will not compile
    fn do_some(&self) {

        // due to this mutation
        // compilator will complain
        // that self should be a mutable reference
        // which violates the original interface
        self.x = 777;
    }
}

fn main() {
    // instantiate the fake implementation
    let fake_some = FakeSome{x: 123};

    // instantiate the main structure
    // NOTICE: it is not declared mutable
    let foo: Foo<FakeSome> = Foo {sub_foo: &fake_some};

    // check the value before using the main functionality
    println!("{:?}", fake_some.x);

    // use the main functionality
    // that sub-utilizes the fake implementation
    foo.do_foo();

    // check the value after using the main functionality
    println!("{:?}", fake_some);
}
