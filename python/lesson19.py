# Lesson 19 - Comprehensions (Stage 2)

def main():
    nums = [1, 2, 3, 4, 5, 6]
    squares = [n * n for n in nums]
    print(squares)
    evens = [n for n in nums if n % 2 == 0]
    print(evens)

    labels = ["py", "js", "go"]
    dict1 = {label: len(label) for label in labels}
    print(dict1)

    print({f for f in "Banana".lower()})
if __name__ == '__main__':
    main()
