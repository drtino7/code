fn main() {
    let var = 1;
    let mut var = 1;
    // signed integers: represents positive and negative numbers
    // unsigned integers: only positive numbers
    let var: i8 = 1;
    let var: u8 = 1;
    let var: i16 = 1;
    let var: u16 = 1;
    let var: i32 = 1;
    let var: u32 = 1;
    let var: i64 = 1;
    let var: u64 = 1;
    let var: i128 = 1;
    let var: u128 = 1;
    let var: isize = 1; 
    let var: usize = 1;  
    let var = 1_000_000_000_000_000_000_000;

    // floating point numbers
    let var: f32 = 1.0;
    let var: f64 = 1.0;

    //assert!(0.1+0.2==0.3); error, the result is 0.30000000000000004 not 0.3
    //assert!(0.1_f32+0.2_f32==0.3_f32); this is ok;
    //assert!(0.1 as f64+0.2as f64==0.3as f64);
    
}
