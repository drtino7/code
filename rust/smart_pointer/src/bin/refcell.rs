use std::cell::RefCell;

fn main() {
    let refcell = RefCell::new(String::from("hello"));
    
    //THIS CRESH, follow ownership rules at compile time.
    // let refcell_1 = refcell.borrow();
    // let mut refcell_2 = refcell.borrow_mut();
    // *refcell_2 = 77;
    // println!("{}",refcell_1);
      
    //in contrast to cell, refcell allow us to modify values that donr implement copy trait.
    //allow to mutate inmutable values
    let mut ref_cell = refcell.borrow_mut();
    *ref_cell = String::from("world");
    println!("{}",ref_cell);
}
