fn main() {
    //clousers
    //functions that can access variables outside of their scope

    lex x: i32 = 1;
    let clouser = | val | val + x;
    let clouser_anotated = |val: i32| -> i32 {val + x};
    println!("{}", clouser(2));
    println!("{}", clouser_anotated(2));

    //cant use a clouser with different types

    let clouser = move || println!("{}", x);
    //cant not use x anymore

    fn fnonce<F>(x: F)  where F: FnOnce(usize) -> bool{ // takes a clouser can be called only once
        x(10)
    }
    fnonce(|x| x == 10);

    fn Fn_mut<F>(x: F)  where F: FnMut(usize) -> bool{ // takes a clouser can be called multiple times
        x(10)
    }
    Fn_mut(|x| x == 10);

    fn Fn<F>(x: F)  where F: Fn(usize) -> bool{ // takes a clouser can be called multiple times
        x(10)
    }
    Fn(|x| x == 10);

    fn create_fn () -> Box<dyn Fn(i32) -> i32> {
        let x = 5;
        Box::new(move |y| x + y)
    }

    let fn_plain = create_fn();



}
