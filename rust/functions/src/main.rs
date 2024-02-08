fn main() {

    fn sum(x: i32, y:i32) -> i32 {
        x + y
    }

    println!("{}", sum(1, 2));

    fn never_return() -> ! {
        panic!("this function never returns")
        unimplemented!()
        todo!()
    }

}
