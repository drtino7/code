fn main() {
    let mut game: Vec<Vec<i32>> = vec![vec![1,2,3],vec![4,5,6],vec![7,8,9]];
    println!("{:?}", game);

    for col in game.iter() {
        for row in col.iter(){
            println!("{}", row);
        }
    }

    let seven = game[2][0];
    println!("{}", seven);
}
