fn main() {
    //flow control
    let n:i32 = 5;
    if n > 5 {
        println!("n is greater than 5");
    } else if n == 5 {
        println!("n is equal to 5");
    } else {
        println!("n is less than 5");
    }

    let big_n = if n < 4 {
            10
        }
        else{
            5
        };
    for n in 1..=100{
        println!("{}", n);
    }

    let names: [String;3] = [String:from("juan"),String::from("valentino"),String::from("roberto")];

    for name in &names{
        println!("{}", name);
    }

    println!("{}",names)

    let numbs: [i32;4] = [4,3,2,1];
    for (index,value) in numbs.iter().enumerate(){
        println!("{} is at index {}",value,index);
    }
    let i:u8 = 0;
    while i < 10{
        println!("{}",i);
        i+=1;
    }

    let mut j:u8 = 0;
    
    for i in 0..100{
        if i == 77{
            break;
        }
        else{
            println!("{}",i);
        }
    }
    for i in 0..100{
        if i == 77{
            continue;
        }
        break;
    }

    loop{
        println!("hello");
        break;
    }

    let i = loop{
        break 5;
    };
    'outer:loop{
        println!("hello");
        'inner:loop{
            break 'outer;
        }
    }
}
