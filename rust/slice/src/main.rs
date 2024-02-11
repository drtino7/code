fn main() {

    //slice
    //similar to arrays, size its not fixed
    let array: [i32;5] = [1,2,3,4,5];
    let slice: &[i32] = &array[..2];
    let s: String = String::from("hello");
    let slice2: &str = &s[..3];

}
