/*
Iterations - Transform - Fuse

Demonstration requires a custom iterator.
Fuse is to be for custom iterators.
*/

use std::iter::{Copied, Fuse, Iterator};

struct MyIterator<'a> {
    responses: Copied<std::slice::Iter<'a, Option<u16>>>,
}

impl<'a> MyIterator<'a> {
    fn new(responses: &'a Vec<Option<u16>>) -> Self {
        Self {
            responses: responses.iter().copied(),
        }
    }
}

impl<'a> Iterator for MyIterator<'a> {
    type Item = u16;

    fn next(&mut self) -> Option<Self::Item> {
        let maybe_response = self.responses.next();

        match maybe_response {
            Some(response) => response,

            None => None,
        }
    }
}

fn main() {
    let responses: Vec<Option<u16>> = vec![Some(11), Some(22), None, Some(33), Some(44)];
    let my_iterator = MyIterator::new(&responses);

    let mut fuse_iterator: Fuse<MyIterator> = my_iterator.fuse();

    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
    println!("{:?}", fuse_iterator.next().ok_or(None::<()>));
}
