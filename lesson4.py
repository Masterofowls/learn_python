# Lesson 4 - Loops

n = int(input("Integer: "))

for i in range(1, n + 1):
    print(i)

count = n                     
while count > 0:
    print(count)
    count -= 1
print("liftoff")


total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum: {total}")