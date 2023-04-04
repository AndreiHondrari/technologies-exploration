/*
Smart pointers - reference cycles

In order to be able to point two structures to each other
there are a few conditions that need to be met:
- the structure lives under a smart pointer (on the heap)
- the smart pointer holding the structure must allow for multiple
  references (therefore std::rc::Rc - reference counting pointer)
- the pointer pointing to another structure from within the structure
  must allow interior mutability, meaning it must allow
  alteration of the inner pointer without requiring mutability
  or without being bothere by the ownership mechanism.
  (RefCell serves this purpose)

Steps:
 - create the two nodes, where one points to None and the other points to the first one
 - borrow as mutable the reference contained by
   the RefCell of the first node, that points to None
 - dereference the mutable reference and change it's value to point to the second node
 - congratulations! you have now achieved a reference cycle

Once a reference cycle is achieved, the RefCells owned by the two nodes will hold each other
in memory indefinitely, therefore creating a MEMORY LEAK.
*/

use std::cell::RefCell;
use std::cell::Ref;
use std::cell::RefMut;
use std::rc::Rc;
use std::ops::Deref;

#[derive(Debug, PartialEq)]
struct Node {
    name: String,
    next: RefCell<Rc<Option<Node>>>
}

const HARD_LIMIT: u8 = 10;

fn traverse(node: &Node, level: u8) {
    println!("NODE | {:?}", node.name);
    if level >= HARD_LIMIT {
        panic!("Too many traverses");
    }
    let next_ref: Ref<Rc<Option<Node>>> = node.next.borrow();
    let next_option: Option<&Node> = (*(*next_ref)).as_ref();
    if next_option != None {
        let next_node: &Node = next_option.unwrap();
        traverse(next_node, level + 1);
    }
}

fn main() {
    /*
    Create our two Nodes on the heap.
    'a' points to None.
    'b' points to 'a'.
    */
    let a = Rc::new(
        Some(Node {
            name: String::from("Gandalf"),
            next: RefCell::new(Rc::new(None))
        })
    );

    let b = Rc::new(
        Some(Node {
            name: String::from("Salvatore"),
            // notice the reference clone
            // 'b' points to 'a' through 'next'
            next: RefCell::new(Rc::clone(&a))
        })
    );

    let a_opt_ref: &Option<Node> = a.deref();
    let a_opt: Option<&Node> = a_opt_ref.as_ref();
    let a_node: &Node = a_opt.unwrap();
    println!("{:?} -> {:?}", a_node.name, a_node.next);

    let b_opt_ref: &Option<Node> = b.deref();
    let b_opt: Option<&Node> = b_opt_ref.as_ref();
    let b_node: &Node = b_opt.unwrap();
    println!("{:?} -> {:?}", b_node.name, b_node.next);

    // create a reference cycle
    // 'a' points to 'b' and 'b' points to 'a'
    {
        println!("Create a reference cycle | a->b->a->b...");
        let mut a_next: RefMut<Rc<Option<Node>>> = a_node.next.borrow_mut();
        *a_next = Rc::clone(&b);
    }

    // traverse the cycle until a limit is hit
    println!("\nStart traversing");
    traverse(a_node, 0);

    println!("\nEND");
}
