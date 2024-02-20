fn main() {
   //traits
   //set of methods that can be implemented for multiple types. similar to classes

   //derived traits
   //debug, clone, copy, PartialEq, Eq, PartialOrd, Ord, Hash
   trait Animal{
      fn sound(&self) -> String;
   }
   
   struct Sheep;
   struct Cow,

   impl Animal for Sheep{
      fn sound(&self) -> String{
         "baa".to_string()
      }
   }

   impl Animal for Cow{
      fn sound(&self) -> String{
         "moo".to_string()
      }
   }

   fn some_func<T: Display + Clone, U: Clone>(a: T, b: U) -> (T, U){
      (a, b)
   }
   fn some_func_where<T,U>(a: T,b: U) -> (T,U) 
   where T: Display + Clone,
   U: Clone,
   {
      (a, b)
   }

   
   fn summary<T>(a: &T) where T: Animal{ //a must implement from Animal
      println!("{}", a.sound());
   }

   let sheep: Sheep = Sheep{};
   let cow: Cow = Cow{};
   summary(&sheep);
   summary(&cow);

   //trait objects
   //its a pointer to any type that implements the given trait

   fn return_animal(s: &str) -> Box<dyn> Animal{
      if s == "cow"{
         Box::new(cow{})
      }else{
         Box::new(sheep{})
      }
   }

   println!("{}", return_animal("cow").sound());
   let animal: Box<dyn Animal> = return_animal("sheep");
   }
