import math
import sys

dimension = int(input("Enter the dimension from 1D to 3D: "))

if dimension < 1 or dimension > 3:
    print("Please enter a valid choice of dimensions between 1 to 3!!!")
    sys.exit()

def DerivativeApproximation(f, x, y, z, h):

    if dimension == 1:

        print("\n==== CHOOSE APPROXIMATION METHOD ====")
        print("1. Forward")
        print("2. Backward")
        print("3. Central")

        choice = int(input("Enter your choice between 1 to 3: "))

        if choice == 1:
            return (f(x+h) - f(x))/h
        elif choice == 2:
            return (f(x) - f(x-h))/h
        elif choice == 3:
            return (f(x+h) - f(x-h))/(h*2)
        else:
            print("Please enter a valid choice between 0 to 3!!! ")
            sys.exit()


    if dimension == 2:
        print("\n==== CHOOSE DIFFERENTIATION METHOD ====")
        print("1. Differentiate with respect to x")
        print("2. Differentiate with respect to y")

        choice = int(input("Enter your choice between 1 to 2: "))

        if choice == 1:
            return (f(x+h, y) - f(x-h, y))/(2*h)
        elif choice == 2:
            return (f(x, y+h) - f(x, y-h))/(2*h)
        else:
            print("Please enter a valid choice between 1 to 2!!! ")
            sys.exit()

    if dimension == 3:

        print("\n==== CHOOSE DIFFERENTIATION METHOD ====")
        print("1. Differentiate with respect to x")
        print("2. Differentiate with respect to y")
        print("3. Differentiate with respect to z")

        choice = int(input("Enter your choice between 1 to 3: "))

        if choice == 1:
            return (f(x+h, y, z) - f(x-h, y, z))/(2*h)
        elif choice == 2:
            return (f(x, y+h, z) - f(x, y-h, z))/(2*h)
        elif choice == 3:
            return (f(x, y, z+h) - f(x, y, z-h))/(2*h)
        else:
            print("Please enter a valid choice between 1 to 3!!! ")
            sys.exit()

    # ===============================================================================================================================================================
    # FUNCTION INPUT
    # ===============================================================================================================================================================

if dimension == 1:
    expression = input("Enter the function f(x): ")
elif dimension == 2:
    expression = input("Enter the function f(x, y): ")
else:
    expression = input("Enter the function f(x, y, z): ")

allowed = {
    "x" : None, 
    "y" : None,
    "z" : None,
    "sin" : math.sin,
    "cos" : math.cos,
    "tan" : math.tan,
    "sqrt" : math.sqrt,
    "asin" : math.asin,
    "acos" : math.acos,
    "atan" : math.atan,
    "log" : math.log,
    "exp" : math.exp,
    "pi" : math.pi,
    "e" : math.e
}

if dimension == 1:

    def f(x):
        values = allowed.copy()
        values["x"] = x
        return eval(expression, {"__builtins__": {}}, values)

elif dimension == 2:

    def f(x, y):
        values = allowed.copy()
        values["x"] = x
        values["y"] = y
        return eval(expression, {"__builtins__": {}}, values)

else:

    def f(x, y, z):
        values = allowed.copy()
        values["x"] = x
        values["y"] = y
        values["z"] = z  
        return eval(expression, {"__builtins__": {}}, values)

x = float(input("Enter the value of x: "))

if dimension >= 2:
    y = float(input("Enter the value of y: "))
else:
    y = 0

if dimension == 3:
    z = float(input("Enter the value of z: "))
else:
    z = 0 

h = float(input("Enter the value of h: "))
if h ==0:
    raise ZeroDivisionError

result = DerivativeApproximation(f, x, y, z, h)
print(result)