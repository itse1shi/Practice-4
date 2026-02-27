import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1
a = dx*dx + dy*dy
b = 2*(dx*x1 + dy*y1)
c = x1*x1 + y1*y1 - r*r
discriminant = b*b - 4*a*c

if discriminant <= 0:
    # Either no intersection or tangent
    if x1*x1 + y1*y1 <= r*r and x2*x2 + y2*y2 <= r*r:
        length = math.hypot(dx, dy)
    else:
        length = 0.0
else:
    sqrt_d = math.sqrt(discriminant)
    t1 = (-b - sqrt_d) / (2*a)
    t2 = (-b + sqrt_d) / (2*a)
    t_start = max(0.0, min(t1, t2))
    t_end = min(1.0, max(t1, t2))
    if t_start > t_end:
        length = 0.0
    else:
        px1 = x1 + dx * t_start
        py1 = y1 + dy * t_start
        px2 = x1 + dx * t_end
        py2 = y1 + dy * t_end
        length = math.hypot(px2 - px1, py2 - py1)

print("%.10f" % length)