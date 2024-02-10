fn main() {
  // String is a heap-allocated, its mutable
  // &str is an imutable not own string
  
  let s = String::from("hello world");

  let hello = &s[0..5];
  let world = &s[6..11];

  let mut s: String = String::from("hello");
  s.push_str(", world");
  s.push('!');
  s.replace("!", "!!");
  let hello = "hello";
  let hello: String = hello.to_string(); // &str -> String // String::from(hello);
  
  let byte_escape = "im am writing ru\x73\x74";
  let unicode_codepoint = "\u{211D}";
  let character_name = "\"DOUBLE-STRUCK CAPITAL R \"";
  let long_string = "string literals
  can span multiple
  lines
  without";
  let raw_str = r"Escapes don't work here: \x3F \u{211D}";
  let byte_string = b"this is a byte string";
  let byte_string = br"this is a raw byte string";
  let s = "hello, 😎";
  let hello = &s[0..6];
  let emoji = &s[6..11]; // emojis or other caracters ocupe more bites
  for character in "hello, world!".chars(){
      println!("{}",character);
  }
}
