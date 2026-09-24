# Lesson 5 - Lists

fruits = ['apple', 'peach', 'banana']
print(fruits[0],fruits[-1])

fruits.append('orange')
print(fruits)

new = input('one more fruit')
if new in fruits:
    print('found')
else:
    print('not found')

for fruit in fruits:
    print(f'- {fruit}')