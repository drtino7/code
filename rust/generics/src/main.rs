fn main() {
    //generics

    struct Elements<T>(T);
    impl<T: std::fmt::Display> Elements<T>{
        fn print(&self){
            println!("{}", self.0);
        }
    }

    let e = Elements("hello");
    e.print();
    let e = Elements(10);
    e.print();
    let e = Elements(true);
    e.print();
    let e = Elements(10.5);
    e.print();

    let sum = sum(10.7,20.5);
    println!("{}", sum);


    #[derive(Debug)]
    struct Point<T, U>{
        x: T,
        y: U,
    }

    //let p: Point<i32,String> = Point{x: 10, y: String::from("hello")};
    //println!("{:?}", p);

    impl<T,U> Point<T, U> {
        fn mixup<V,W>(self, y: Point<V, W>) -> Point<T, W>{
            Point{
                x: self.x,
                y: y.y,
            }   
    }
    }

    //const generic
    

}

fn sum<T: std::ops::Add<Output = T>>(x:T,y:T) -> T{
    x+y
}

