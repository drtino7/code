use std::rc::Rc;

#[derive(Debug)]
struct Node{
    value: String,
    sons: Option<Vec<Rc<Node>>>,
}

fn main() {
    
    //to conclude: rc allows developers to have a shared reference to an inmutable value.
    // works like a garbash collector.
    // when using clone method gives a reference and not a copy, everyone ones the value

    let son_1 = Rc::new(Node{
        value: String::from("1"),
        sons: None,
    });

    let son_2 = Rc::new(Node{
        value: String::from("2"),
        sons: None,
    });
    
    let node = Rc::new(Node{
        value: String::from("3"),
        sons: Some(vec![son_1.clone(),son_2.clone()])
    });
    
    let mut frontair = vec![son_1.clone(),son_2.clone()];
    dbg!(frontair);



    let a = String::from("hello");
    let b = &a;


    fn print(mut value: String) -> String{
        value
    }

    //print(*b);
    print(node.value.clone());
    // as we can see rc provides the ownership. as a shared reference dont so we can't move it.
}

