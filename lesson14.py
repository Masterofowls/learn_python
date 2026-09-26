# Lesson 14 - Sets (Stage 2)
def main():
    nums = [1, 2, 2, 3, 4, 4, 5]

    unique = set(nums)
    print(unique)

    a = {1, 2, 3}
    b = {3, 4, 5}

    print(a | b, a & b, a - b)

    number = int(input('number: '))

    if number in unique:
        print('in set')
    else:
        print('not in set')
    unique.add(number)      # always OK — sets ignore duplicates
    print(unique)

if __name__ == "__main__": main()