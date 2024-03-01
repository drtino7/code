fn main() {
    let s: &str = "hello";
    let s1: String = format!("{} world!",s);
    //debug and display

    struct no_debug(i32);
    
    #[derive(Debug)]
    struct yes_debug(i32);

    print!("{:?}",yes_debug(7)) //:#? pretty debug

    struct hi(i32);
    struct hi_(hi;

    impl std::fmt::Debug for hi_{
        fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result{
            write!(f, "{}", self.0.0)
        }
    }

    struct Point2D{
        x: i32,
        y: i32,
    }

    impl std::fmt::Display for Point2D{
        fn fmt(&self, f: &mut std::fmt::Formatter ) -> std::fmt::Result{
            wrtite!(f,"Display: {} + {}i", self.x, self.y)
        }
    }
}
