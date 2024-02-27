pub fn fix_incorrect_order(){
    cook_order();
    //or use crate::etc
    super:front_of_house::serving::serve_order(); // access to super module so front_of_house module
}

pub fn cook_order(){}
