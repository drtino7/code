fn main() {
    //char
    let char: char = 'a'; // rust diferences between single and double quotes
    println!("{}",size_of_val(&char));

    //bool
    let bool1: bool = true;
    let bool2: bool = false;
        //operators
    println!("{}",bool1 && bool2);
    println!("{}",bool1 || bool2);
    println!("{}",!bool1);
    let bool3: bool = bool1 ^ bool2;

    //unit type
    let unit: () = (); //its empy, has no value
              
                      
}
