from math import sqrt

def quadratic_equation_solver(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    discriminant = sqrt((b**2) - (4*a*c))
    if discriminant >= 0:
        x1 = ((-b) + discriminant) / (2*a)
        x2 = ((-b) - discriminant) / (2*a)
        if x1 == x2:
            return x1
        else:
            return x1, x2
    else:
        print("This equation has no real roots.")

x,y,z = input().split()
print(quadratic_equation_solver(x,y,z))
