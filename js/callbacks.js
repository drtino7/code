function show (numb) {
  console.log(numb);
}

function add(a,b,callback){
  let sum = a + b;
  callback(sum);
}

add(1, 2, show);
