# Lesson 9 - Errors

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
    
text1 = input('text: ')
result = safe_int(text1)

if (result == None):
    print('Invalid number')
else:
    print(f"double = {result * 2}")

try:
    with open("missing_file.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")