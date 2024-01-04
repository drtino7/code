fn main() {

    //unmutable
    let original = String::from("originsl__");
    let copy = cal( &originsl );

    fn call(copy: &String) -> usize{
        copy.len()
    }
    //mutable
    let mut m = 5;
    {
        let y = &mut x;
        *y += 1;
    }
    prinln!("{}",x); // x + 1



}
