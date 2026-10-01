# Lesson 15 - Tuples (Stage 2)

def bounds(nums):
    return min(nums), max(nums)

def main():
    point = (4, 9)
    x, y = point
    print(x, y)

    lo, hi = bounds([5, 2, 9, 2])
    print(lo, hi)

    places = {
        (0, 0): "origin", 
        (1, 2): "A"
    }
    print(places[(1, 2)])

    lst = list((1, 2, 3))
    lst.append(4)
    print(tuple(lst))

if __name__ == "__main__":
    main()