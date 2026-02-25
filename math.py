import math

degree = float(input())

radian = math.radians(degree)
print(round(radian, 6))

###########################################

height = float(input())
base1 = float(input())
base2 = float(input())

area = (base1 + base2) * height / 2
print(area)

###########################################

import math

n = int(input())
side = float(input())

area = (n * side**2) / (4 * math.tan(math.pi / n))
print(area)

###########################################

import math

base = float(input())
height = float(input())

area = base * height
print(area)