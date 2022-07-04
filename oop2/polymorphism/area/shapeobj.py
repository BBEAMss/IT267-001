from shapetype import *

#Menu
print('===== Compute area =====')
print('1) Square')
print('2) Circle')
print('3) triangle')
choice = int(input('Enter choice (1-3): '))
print('==========================')

#check choice
if choice == 1:
    s = Square()
    s.length = float(input('Enter length: '))
    s.print_square()
elif choice == 2:
    c = Circle()
    c.radius = float(input('Enter radius: '))
    c.print_circle()
elif choice == 3:
    t = Triangle()
    t.base = float(input('Enter base: '))
    t.high = float(input('Enter high: '))
    t.print_triangle()
else:
    print('Wrong choice!!!!')