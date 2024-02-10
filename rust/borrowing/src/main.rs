fn main() {
 //borrowing 
 //its a way to temporality access a data without taking ownership
 //when borrowing you are taking a reference(pointer) to the data
 //data can bve borrowed as mutable or unmutable
 
 //borrowing rules
 // 1. at any given time, you can have eiher ONE mutable reference OR any number of immutable references
 // 2. references must always be valid
 
 let s1: String = String::from("hello"); 

 let len: 132 = calculate_len(&s1);

 println!("length of {} is {} ", s1, len);
 
 let mut s = String::from("hello");
 change_s(&mut s);

// let mut r1 = &mut s; error because we can only have one mutable reference
// let mut r2 = &mut s;


// let r1 = &s; // no problem
// let r2 = &s; // no problem
// let r3 = &mut s; // BIG PROBLEM 

// dangling
// let reference_to_nothing = dangle();
// let reference_to_nothing = no_dangle();

// fn dangle() -> &String{ # reference_to_nothing its a pointer of s; however s is not in scope, so
// when the function ends, s will be deallocated, so we cant assign a pointer to a future dead
// variable
//     let s = String::from("hello");
//     &s
//}


// fn no_dangle() -> String{
//     String::from("hello")
//     s
//}

    let x: 132 = 5;
    let p: &i32 = &x; // memory address
    let q: &i32 = *x; // value

}


fn calculate_len(s: &String) -> i32{ // s = 0x0004
    s.len()
}
fn change_s(s: &mut String){
    s.push_str(", world");
}
