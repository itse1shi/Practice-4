import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def line_circle_intersect(x1,y1,x2,y2,r):
    dx, dy = x2-x1, y2-y1
    a = dx*dx + dy*dy
    b = 2*(dx*x1 + dy*y1)
    c = x1*x1 + y1*y1 - r*r
    disc = b*b - 4*a*c
    if disc < 0:
        return False
    t1 = (-b - math.sqrt(disc)) / (2*a)
    t2 = (-b + math.sqrt(disc)) / (2*a)
    return (0 <= t1 <= 1) or (0 <= t2 <= 1)

if line_circle_intersect(x1,y1,x2,y2,r):
    d1 = math.hypot(x1, y1)
    d2 = math.hypot(x2, y2)
    cross = x1*y2 - x2*y1
    theta = abs(math.atan2(cross, x1*x2 + y1*y2))
    alpha1 = math.acos(r/d1)
    alpha2 = math.acos(r/d2)
    arc = max(0.0, theta - alpha1 - alpha2)
    length = math.sqrt(d1*d1 - r*r) + math.sqrt(d2*d2 - r*r) + r*arc
else:
    length = dist((x1,y1),(x2,y2))

print("%.10f" % length)