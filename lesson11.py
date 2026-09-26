# Lesson 11 - Classes


class Learner:
    def __init__(self, name, lesson):
        self.name = name
        self.lesson = lesson

    def info(self):
        return(f"{self.name} is on lesson {self.lesson}")
    
    def advance(self):
        self.lesson += 1

def main():
    learner1 = Learner('Dan', 11)
    print(learner1.info())
    learner1.advance()
    print(learner1.info())

if __name__ == "__main__":
    main()