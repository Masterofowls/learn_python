# Lesson 10 helpers
def double(n):
    return n * 2

def clamp(n, low, high):
    if n < low:
        return low
    if n > high:
        return high
    else:
        return n
