fn main() {
    //method

    #[derive(Debug)]
    struct Rectangle{
        base: u32,
        height: u32,
    }
    impl Rectangle{
        fn area(&self) -> u32{ // &mut self
            self.base * self.height
        }
        fn new(base: u32, height: u32) -> Self{
            Self{
                base,
                height,
            }
        }
    }

    let r = Rectangle{
        base: 10,
        height: 20,
    };
    let r: Rectangle = Rectangle::new(10, 20);
    println!("{:?}", r);
    println!("{}", r.area());


}
