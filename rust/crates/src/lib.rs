pub mod front_of_house;
pub mod back_of_house;

pub fn eat_at_restaurant(){
    //absolute path
    crate::front_of_house::hosting::add_to_whitelist();
    //relative path
    front_of_house::hosting::add_to_whitelist();
}