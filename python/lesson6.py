# Lesson 6 - Dicts and tuples

student = {
    'name': 'Dan',
    'lesson': 6,
    'score': 60
}
print(f'{student['name']}, scored {student['score']} on lesson {student["lesson"]}')

if (student['score'] >= 50):
    student['passed'] = True
else:
    student['passed'] = False

for key, value in student.items():
    print(key, value)

levels = ("beginner", "intermediate", "advanced")
print(levels[0])