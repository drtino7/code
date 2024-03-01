fn main() {
    // lifetimes
    //used to specify that a reference or a pointer is valid for a certain period of time
    //prevents null pointers

    fn _print<'a>(x: &'a i32) -> () {
        println!("{}",x);
    }

    fn _return_x<'a, 'b>(x: &'a i32, _: &'b i32) -> &'a i32{ //return value must have the correct lifetime
        x
    }

    struct Person<'a>{
        name: &'a str
}


//lifetime elision
//three rules
//1. each parameter that is a reference gets its own lifetime parameter
//2. if there is exactly one input parameter, that lifetime is assigned to all output parameters
//3. if there are multiple input parameters, but one of them is &self or &mut self, the lifetime of self is assigned to all output parameters
//IF ANY OF THIS RULES DOES NOT APPLY, THE PROGRAMMER HAS TO SPECIFY THE LIFETIME

//static lifetimes
//lives on the entire program
}