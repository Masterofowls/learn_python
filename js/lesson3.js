// Lesson 3 - If and else
function main(){
    const number = -3
    if (number > 0){
        console.log('Positive')
    } else if (number === 0){
        console.log('Zero')
    } else {
        console.log('Negative')
    }

    if (number % 2 == 0){
        console.log('Even')
    } else {
        console.log('Odd')
    }
}
main()