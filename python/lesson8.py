# Lesson 8 - Files

name = input("username: ")
with open('learner.txt', 'w', encoding='utf-8') as f:
    f.write(f'name {name}\n')
    f.write('lesson: 8\n')

with open('learner.txt', 'r', encoding='utf-8') as f:
    content = f.read()      
print(content)

with open('learner.txt', 'a', encoding='utf-8') as f:
    f.write('status: learning\n')

with open('learner.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

