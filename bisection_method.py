#bisection method = root-finding algorithm
#applies to continuous function/interval where value of function changes sign from a to b
#process of updating start and end until error is acceptably low
#complexity: logn

#function= cont. func, a=lower bound, b=upper bound, tolerance=acceptable error
def bisection(function, a, b, tolerance):
    
    def f(x): #helper function to turn user's input str function into a math function
        f = eval(function)
        return f

    error = abs(b - a) #ensure user's current level of error is not greater than acceptable amt 

    while error < tolerance:
        c = (a + b) / 2 #midpoint between a and b

        if f(a) * f(b) >= 0:
        #more than 1 root, or no roots
            print("No real roots or multiple roots.")
            break

        elif f(a) * f(c) < 0:
            b = c
            error = abs(b - a)
        
        elif f(b) * f(c) < 0:
            a = c
            error = abs(b - a)

        else:
            print("Error")
            break

    print(f"The error is {error}")
    print(f"Ther lower boundary is {a} and the upper boundary is {b}")
