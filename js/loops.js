let arr = [1,2,3];

for (let i = 0; i<arr,length; i++){
    console.log(arr[i]);
}

for (let i of arr){
    console.log(i);
}

class   Car{
    constructor(model, color, year){
        this.model = model;
        this.color = color;
        this.year = year;
    }
}

let car = new Car("mustang", "red", 2020);

for (let i in car){
    console.log(i);
}

while (i < arr.length){
    console.log(arr[i]);
    i++;
} 

do{
    console.log(arr[i]);
    i++;
} while (i < arr.length)