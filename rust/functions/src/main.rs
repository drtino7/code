fn main() {
    //creatig function
    fn print_number(x: i32){
        println!("the number is: {}",x);
    }
//calling the function
    print_number(7);

                        // what the func returns
    fn add_number(x: i8) -> i8{
        x + 1
    }
    let _var = add_number(7);

    fn get_values() -> (i32, i32) {
        (42, 77)
    }
    //clousere

                    //parameters// what to do
    let _add_one = |x: i32|         x +1;
    let _add_two = |x|{
        let mut result: i32 = x;
        result += 1;
        result += 1;
        result
    };

}
