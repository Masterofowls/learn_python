// Lesson 4 - Loops
function main(){
    let n = 3;
    for (let i = 1; i <= n; i++){
        console.log(i)
    }
    while (n > 0) {
        console.log(n);
        n = n - 1; 
    }
    console.log("liftoff");
    let a = 3
    let total = 0;
    for (let i = 1; i <= a; i++) {
    total += i;
}
console.log(total);  
}
main()