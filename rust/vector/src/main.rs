fn main() {
    //vector 
    //alocated in heap,dinamically sized, every type must be the same
    let arr: [u8; 10] = [1,2,3,4,5,6,7,8,9,10];
    let _vector: Vec<u8> = Vec::from(arr);
    let _v: Vec<u8> = vec![1,2,3,4,5];
    let v: Vec<u8> = vec!(1,2,3,4,5,7);
    let mut vec = vec![];

    for i in &v{
        vec.push(*i);
    }
    vec.pop();
    vec.get(0); //return an option Some - None

    let mut vec = Vec::from([1,2,3]);
    for i in 0..5{
        match vec.get(i){
            Some(x) => vec[i] = x+1,
            None => vec.push(i+2), 
        }
    }

    let mut v: VEc<u8> = vec![1,2,3];
    let slice: &[u8] = &v[..];

    let mut vec = Vec::with_capacity(10);
}