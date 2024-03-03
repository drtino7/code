const age = 18

if (age >= 18) {
    console.log("you can drive")
} else if( age < 18) {
    console.log("you can't drive")
} else {
    console.log("you can't drive")
}

switch (age){
    case 17:
        console.log("you can't drive")
        break
    case 18:
        console.log("you can drive")
        break
    default: 
        console.log("you can't drive")
}