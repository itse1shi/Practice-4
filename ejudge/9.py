import math 

def powers_of_two(n):
    for i in range(n + 1):
        yield pow(2, i)

n = int(input())

print(*powers_of_two(n), sep=" ")