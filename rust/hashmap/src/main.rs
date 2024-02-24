use std::collection::HashMap;

fn main() {
    //hashmap
    //similar to python dict
    //has unique key and value
    //key must be hashable

    let mut scores: HashMap<&str, i32> = HashMap::new();
    score.insert("blue", 10);
    score.insert("red", 20);

    let score_blue = score.get("blue"); //returns an option

    if score.contains_key("blue"){
        let score_blue = score.get("blue").unwrap();
        score.remove("blue");
    }

    score.insert("blue", 30);
    let score_blue: i32 = score["blue"];

    for (key, value) in score {
        println!("{}: {}", key, value);
    }

    score.entry("blue").or_insert(40);
}
