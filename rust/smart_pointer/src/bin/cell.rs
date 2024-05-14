use std::cell::Cell;
//cell dont give reference to its value
//not thread safe
// so basically cells allows us to have multiple mutable references to a value
//can not use method get on heap allocations for example String

fn main() {
 
    let cell = Cell::new(7);
    
    let x = &cell;
    let y = &cell;
    let _y = cell.get();
    
    cell.set(8);
    x.set(97);
    y.set(7);
    
    println!("{} and cell is: {}",x.get(),cell.get());

}

