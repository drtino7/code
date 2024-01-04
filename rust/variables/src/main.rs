fn main() {
    let number_decimal = 65.4321_f32;
    //convertion float to int
    let number_integer = number_decimal as u8;
 
    let integer = 10u8;
    let other_integer = 20u16;
    //
    let result = integer as u16 + other_integer; //return 30
    println!("{}",result);
 
    //array
 
    let a = [1,2,3]; // a:[i32:3]
    let mut muted = [1,2,3]; //can change // muted:[i32:3]
     let b = [0;20];  // b[i32:20]
     println!("the size of a is:{}",a.len());
 
     let names = ["juan","pedro","rodr"];
     println!("name 2 is:{}",names[1]);
 
     //slice
     let c = [0,1,2,3,4];
     let complete = &c[..];//all a array
     let middle = &c[1..4];//elemets from 1 to 4 of a array
     let middle = &c[1..=4];//includes 4
 
     //tuple
 
     let x = (1,"hello");
     let y: (i32,&str) = (1,"hello");
     let z: (i32,f64,u8) = (500,6.4,1);
 
     let mut z = (1,2); // can mut
 
     //let (x,y,z) = (1,2,3) // x = 1, y = 2, z = 3;
 
     let tuple = (1,2,3);
     let d = tuple.1; 
 
     let e = 7;
     let e = e + 1 ;
     
     println!("{}",e);
 
     //bool
 
     let flag = true;
     let flag: bool = false;
 
     //char
     let f = 'f';
     let  g: char = 'g';
     let emoji = '😊';
 
     // type
     type NanoSecond = u64;
     type U64 = u64;
     let nanosecode:NanoSecond = 5 as U64;

     // In Rust, data types are fundamental to ensure program safety and performance.

// Unsigned 8-bit integers (0 to 255)
let u8_variable: u8 = 42;

// Unsigned 16-bit integers (0 to 65,535)
let u16_variable: u16 = 1000;

// Unsigned 32-bit integers (0 to 4,294,967,295)
let u32_variable: u32 = 4294967295;

// Unsigned 64-bit integers (0 to 18,446,744,073,709,551,615)
let u64_variable: u64 = 18446744073709551615;

// Architecture-sized unsigned integers (depends on the operating system)
let usize_variable: usize = 100;

// Signed 8-bit integers (-128 to 127)
let i8_variable: i8 = -50;

// Signed 16-bit integers (-32,768 to 32,767)
let i16_variable: i16 = 3000;

// Signed 32-bit integers (-2,147,483,648 to 2,147,483,647)
let i32_variable: i32 = -2147483648;

// Signed 64-bit integers (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
let i64_variable: i64 = 9223372036854775807;

// Architecture-sized signed integers (depends on the operating system)
let isize_variable: isize = -200;

// 32-bit floating-point numbers
let f32_variable: f32 = 3.14;

// 64-bit floating-point numbers
let f64_variable: f64 = 2.71828;

// Unicode character (stores a single character)
let char_variable: char = 'A';

// Boolean (true or false)
let bool_variable: bool = true;

// Strings (immutable collection of characters)
let string_variable: &str = "Hello, Rust!";

// Tuple (ordered collection of heterogeneous elements)
let tuple_variable: (i32, f64, char) = (42, 3.14, 'X');

// Fixed-size array (homogeneous collection of elements with a fixed size)
let array_variable: [i32; 5] = [1, 2, 3, 4, 5];
 

 let string: String = String::from("string"); 
    } 