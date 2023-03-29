/*
smart pointers - reference count
*/


use std::rc::Rc;

#[derive(PartialEq)]
struct Node {
    name: String,
    next: Option<Rc<Node>>
}

fn traverse(node: &Rc<Node>) {
    println!("{}", node.name);
    if node.next != Option::None {
        traverse(node.next.as_ref().unwrap());
    }
}


fn main() {
    /*
    x ━━━┓
         ┃
         a ━━ b ━━ c
         ┃
    y ━━━┛
    */
    let c = Rc::new(Node {
        name: String::from("C"),
        next: Option::None
    });
    let b = Rc::new(Node {
        name: String::from("B"),
        next: Option::Some(Rc::clone(&c))
    });
    let a = Rc::new(Node {
        name: String::from("A"),
        next: Option::Some(Rc::clone(&b))
    });

    let x = Rc::new(Node {
        name: String::from("X"),
        next: Option::Some(Rc::clone(&a))
    });
    let y = Rc::new(Node {
        name: String::from("Y"),
        next: Option::Some(Rc::clone(&a))
    });

    println!("\nTraverse from x");
    traverse(&x);

    println!("\nTraverse from y");
    traverse(&y);
}
