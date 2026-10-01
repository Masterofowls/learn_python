# Lesson 20 - args and kwargs (Stage 2)
def main():
    def multiply_all(*args):
        result = 1
        for num in args:
            result *= num
        return result
    
    def describe_person(name, **kwargs):
        print(name)
        for k, v in kwargs.items():
            print(f"{k}={v}")

    print(multiply_all(2, 3, 4))
    print(multiply_all())
    describe_person("Dan", lesson=20, city="TLV")

    vals = [2, 5]
    print(multiply_all(*vals))


if __name__ == '__main__':
    main()