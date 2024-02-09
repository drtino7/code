fn main() {

    //stack memory
    //all data stored in stack kust be fized size like int, char, float
    //stack memory is not dynamic
    //pushing to the stack its fadter than the heap because its aleays on the top
    //if the var is not fixed size ut will create a ponter in the stack referinf to a var in the
    //heap

    //heap 
    //all data is not fixed size
    //its slower to push and searh vars in thr heap
    //return a pointer

  //when creating string the str id not holding the string, only metadata and pointer of the real
  //string. so if whe do this string = String::from("hello"); and string1 = string; then}
  // rust will drop string becose there only can be one owner for a variable. anyway we can do 
  // string1 = string1.clone(); to clone the entire str
  
}
