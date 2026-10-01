// Lesson 5 - Arrays
function main(){
    const fruits = ["apple", "peach", "banana"]
    console.log(fruits[0], fruits[fruits.length - 1])
    fruits.push("orange")
    console.log(fruits)
    const query = "pear"
    if (fruits.includes(query)){
        console.log('found')
    } else {
        console.log('Not found')
    }
    for (let fruit of fruits){
        console.log(`- ${fruit}`)
    }
}
main()