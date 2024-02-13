fn main() {
 //its a compound type taht allow to group togheter values of different types
 //similar to tuples  but every element has its own name
 //have to be inizilitaded with data
 
  let mut user = User {
    String::from("valentino"),
    21,
    String::from("test@test.com"),
  };

    user.name = String::from("juan");
    let mut user: User = create_user(String::from("valentino"), 21, String::from("test@test.com"));
    let user2: User = {
        dgb!(email: String::from("test@test.com")),
        ..user // tekes the rest of the values from the user 1
    };

    struct color (u8, u8, u8);
    let red: color = color(255, 0, 0);
}

//template 
#[derive(Debug)] // implements debug trait
struct User{
    name: String,
    age: u8,
    email: String,
}

fn create_user(name:String, age:u8, email:String) -> User{
    User{ //if names of fields and parameters are the same we can omit the :arg
        name: name,
        age,
        email,
    }
}
