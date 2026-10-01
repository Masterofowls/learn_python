# Lesson 17 - Dicts master (Stage 2)
def main():
    student = {"name": "Dan", "lesson": 17, "score": 80}
    print(student.keys())
    print(student.values())
    student.update({"score": 90, "city": "TLV"})
    student.setdefault("passed", True)
    student.setdefault("passed", False)
    print(student["passed"])
    city = student.pop('city')
    print(city)
    print(student)
    roster = {
        "david": {"lesson": 17, "score": 90},
        "ada": {"lesson": 17, "score": 95},
    }
    print(roster["david"]["score"])
    for k, v in student.items():
        print(k, v)

if __name__ == '__main__':
    main()