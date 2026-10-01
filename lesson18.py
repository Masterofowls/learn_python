# Lesson 18 - String methods (Stage 2)
def main():
    raw = " python,requests,asyncio "
    clean = raw.strip()
    print(clean)
    tools = clean.split(",")
    print(tools)
    print(" | ".join(tools))
    print(clean.replace("python", "Python").upper())
    word = input('word: ')
    if word.lower() in clean.lower():
        print("found")
    else:
        print("not found")

if __name__  == '__main__':
    main()