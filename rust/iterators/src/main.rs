use std::collections::HashMap;

fn main() {
    //iterators 
    //return an option
    let v: Vec<i32> = vec![1,2,3];
    
    for i in v.into_iter() {
        println!("{}", i);
    }

    let mut v: Vec<i32> = vec![1,2,3].into_iter();

    let v1 = v.next()

    // * into_iter, consumes  the collection, its no longer able for reuse, ownership has moved to the loop
    // * iter, borrows the collection
    // * iter_mut, mutably borrows the collection

    struct Counter {
        count: u32,
    }

    impl Iterator for Counter {
        type Item = u32;

        fn next(&mut self) -> Option<u32> {
            if self.count < 5 {
                self.count += 1;
                Some(self.count)
            } else {
                None
            }
        }
    }

    let mut counter = Counter { count: 0 };
    while let Some(v) = counter.next() {
        println!("{}", v);
    }

    let v: Vec<i32> = vec![1,2,3];
    //sum
    let sum: i32 = v.iter().sum(); 
    println!("{}",v);
    //collect
    let v: Vec<i32> = vec!(("juan",18),("maria",20));
    let v: HashMap<String,i32> = v.into_iter().collect();
    println!("{}",v);


    //map
    let v: Vec<i32> = vec![1,2,3];
    let v: Vec<i32> = v.iter().map(|x| x + 1).collect();
    println!("{}",v);

}