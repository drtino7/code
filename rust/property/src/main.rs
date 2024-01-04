fn main() {
    let x = String::from("try"); // x owns try
    let y = x;
    // error: println!("{}",x); x is no longer avaiable

    fn test_(x){
        printnl!("{}",x);
    }

    let x = String::from("try"); // x owns try
    test_(x);
    // now x proper to this function. no more avaiable to the global space
}
