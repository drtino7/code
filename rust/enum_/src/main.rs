fn main() {
    //enum 
    enum ipadr{
        v4(String),
        v6(String),   
    }

    let home: ipadr = ipadr::v4(String::from("127.0.0.1"));
    println!("{}", home);
    let loopback: ipadr = ipadr::v6(String::from("::1"));
    println!("{}", loopback);

    //option
    enum Option<T>{
        Some(T),
        None
    }   

    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);
}

fn plus_one(X: Option<i32>) -> Option<i32> {
    match X {
        None => None,
        Some(i) => Some(i + 1),
    }
}
