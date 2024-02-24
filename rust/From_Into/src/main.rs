fn main() {
    //from - into
    //can be implemented for custom types
    //comes with into

    struct Number{
        value: i32,
    }

    impl From<i32> for Number{
        fn from(m: i32) -> Number{
            Number{
                value: n,
            }
        }
    }

}
