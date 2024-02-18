fn main() {
    //assosiated types
    //allow to specify a ttype that is associated witha the trait 
    
    trait MyTrait {
        type Mytype;

        fn get_my_type(&self) -> Self::Mytype;
    }

    struct Mystruct{}

    impl MyTrait for Mystruct{
        type Mytype = i32;

        fn get_my_type(&self) -> Self::Mytype {
            return 42;
        }
    }

}
