def sq(a, b):
    for i in range(a, b + 1):
        yield i * i

a, b = map(int, input().split())

for num in sq(a, b):
    print(num)