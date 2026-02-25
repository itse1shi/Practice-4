def squares_up_to_n(n):
    for i in range(n + 1):
        yield i*i

n = 5
for sq in squares_up_to_n(n):
    print(sq, end=" ")  # 0 1 4 9 16 25

###########################################

def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())

print(", ".join(str(x) for x in even_numbers(n))) # 0, 2, 4, 6, 8, 10, ... , n

###########################################

def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 50
for num in divisible_by_3_and_4(n):
    print(num, end=" ")   # 0 12 24 36 48

 ###########################################

def squares(a, b):
    for i in range(a, b + 1):
        yield i*i

for val in squares(3, 7):
    print(val)  # 9 16 25 36 49

 ###########################################

def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num, end=" ") # 5 4 3 2 1 0