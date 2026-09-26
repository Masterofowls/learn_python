# Lesson 16 - Lists master (Stage 2)
def main():
    nums = [3, 1, 4, 1, 5]
    nums.append(9)
    nums.extend([2,6])
    print(nums)

    nums.insert(0,0)
    print(nums)

    print(nums.count(1))
    print(nums.index(4))
    print(nums[1:4])
    print(sorted(nums))
    print(nums)
    nums.sort()
    print(nums)

    copy = nums.copy()
    copy.pop()
    print(nums)
    print(copy)

if __name__ == '__main__':
    main()