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

    //if

    //let number = 7;
   // if number{ // need bool
    //    printnl!("{}",number)
    //}

    // > greter than
    // < less than
    // <= less than or equal
    // >= greter than or equal
    // != not equal

    // && and
    // || or
    // ! not


    let var = "juan";
    if var == "roberto"{
        println!("roberto");
    } else if var == "rodrigo"{
        println!("rodrigo");
    } else{
        println!("is not rodrigo nither juan");
    }

    // numb % 4 == 0 // rest

    let condition = true;
    let number = if condition {1} else {0};

    // loop
    
   // loop{
   //     println!{"iteraction"};
   //     if a {
   //         break;
   //     }
  //  }

//    let mut count =  0;
//    let result = loop{
//        count += 1;
//        if count == 10{
//            break count *2;
//        }
//    };
    

//    let mut var = 0;
//    'result : loop{
//        if result == 5{
//            println!("5");
//        }
//        loop{
//            if result == 3{
//                println!("3");
//                continue;
//            }
//            if result == 4{
//                break;
//            }
//            if result == 7{
//                break 'result;
//            }
//        }
//    }

    //while
    let mut numb = 0;
    while numb < 100{
        println!("{}",numb);
        numb += 1;
    }


        //for
    for i in 0..100{
        println!("{}",i);
    }


} 

