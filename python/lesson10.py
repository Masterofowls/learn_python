# Lesson 10 - Modules
# need helpers.py

import math
import helpers

def main():
    print(math.sqrt(49))
    print(helpers.double(6), helpers.clamp(15, 0, 10))

if __name__ == "__main__":
    main()