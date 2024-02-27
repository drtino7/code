mod front_of_house;

fn main() {
    //cargo and modules

    crates::front_of_house::hosting::add_to_whitelist();

    crates::eat_at_restaurant();
}
