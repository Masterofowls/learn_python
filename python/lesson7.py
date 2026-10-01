# Lesson 7 - Functions
def is_even(n):
    if (n % 2 == 0):
        return True
    else:
        return False

def sum_to(n):
    count = 0
    for i in range(1, n+1):
        count+=i
    return count

def describe(name, lesson=7):
    return (f'{name} is on lesson {lesson}')


print(is_even(4))
print(sum_to(5)) 
print(describe("Dan"))
print(describe("Dan", lesson=8))