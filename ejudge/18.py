x0, y0 = map(float, input().split())
x1, y1 = map(float, input().split())
y1_m = -y1
k = (y1_m - y0) / (x1 - x0)
xr = x0 - y0 / k
yr = 0.0
print("%.10f %.10f" % (xr, yr))