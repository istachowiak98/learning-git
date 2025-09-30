a = -100
b = -10
c = -6
delta = b**2-4*a*c
x1 = (-b-delta)/2*a
x2 = (-b+delta)/2*a
x0 = -b/2*a
if delta > 0:
  print(x1, x2)
if delta == 0:
  print(x0)
if delta<0:
  print("Brak")
  print("coś nowego")
  