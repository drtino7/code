use std::num::ParseIntError;

fn main() {
    //errors
    

    //panic! its the simplest error handliing

    //result

    fn divide(x: f32, y: f32) -> Result<f32, &'static str>{
        if y == 0.0{
            Err("Cannot divide by zero")
        }
        else{
            Ok(x / y)
        }
    }

    let result: f32 = divide(10.0,2.0);

    match result{
        Ok(res) => println!("{}", res),
        Err(msg) => println!("{}", msg),
    }

    // the ? operator

    let  str = "10";
    let numb = str.parse::<i32>()?; //if ok return value else return parseinterror
    println!("{}", numb);

    // map _ and_then

    fn add_two(numb: &str) -> i32{
        num = numb::parse<i32>().map(|n| n + 2); // map func ask for a func parameter which is executed return a result
    }
    fn add_two(numb: &str) -> i32{
        num = numb::parse<i32>().and_then(|n| Ok(n + 2)); // and_then func ask for a func parameter which is executed return a result
    }

    type Res<i32> = Result<i32, ParseIntError>;

}
