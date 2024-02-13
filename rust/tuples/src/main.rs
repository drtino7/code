fn main() {
    //tuples
    // store related pieces of info in a var
    // collection o values of different types
    // its fixed size allocated in stack
    // signature is (T,T,T)
    let tuple: (i32, f64, u8) = (-500, 6.4, 1);
    let tuple2: (i32,(f64,u8)) = (-500, (6.4,1));
    println!("{}",tuple.1);
    //long tuples cant print more than 13 elements
    let (x:i32,y:f64,z:u8) = tuple;

    let sum = sum((10,20));
    println!("{}",sum);

    
}

fn sum(nums:(i32,i32)) -> i32 {
    nums.0 + nums.1 // if i want to return a tuple (nums.0 + nums.1,nums.0 - nums.1)
}
