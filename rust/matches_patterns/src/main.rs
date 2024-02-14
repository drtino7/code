enum Coin{
    penny,
    nickel,
    dime,
    quarter,
}
fn main() {
    //matches
    //all cases must be considered
    // we can us _ as else  
    


    let coin: Coin = Coin::penny;
    let value = value_in_cents(coin);
    let alphabet: [char;5] = ['a','b','C','7','e'];
    //for i in alphabet{
        //assert!(matches!(i, 'A'..='Z' | 'a'..='z' | '0'..='9'));
    //}

    let x: Option<i32> = Some(7);
    if let Some(i) = x{
        println!("{}", i);
    }

    

}
fn value_in_cents(coin: Coin) -> u8 {
    match coin{
        Coin::penny => 1,
        Coin::nickel => 5,
        Coin::dime | Coin::quarter => 10,
        _ => 0,
    }
}
