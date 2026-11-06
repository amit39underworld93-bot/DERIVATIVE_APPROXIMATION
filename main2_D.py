import math

def DerivativeApproximation_in_2D(f, x, y, h):

    print("\n==== CHOOSE DIFFERENTIATION METHOD ====")
    print("1. Differentiate with respect to x")
    print("2. Differentiate with respect to y")

    choice = int(input("Enter your choice between 1 to 2: "))

    if choice == 1:
        return (f(x+h, y) - f(x-h, y))/(2*h)
    elif choice == 2:
        return (f(x, y+h) - f(x, y-h))/(2*h)
    else:
        print("Please enter a valid choice between 1 to 2: ")


# ===============================================================================================================================================================
# FUNCTION INPUT
# ===============================================================================================================================================================

expression = input("Enter the function f(x,y): ")

allowed = {
    "x" : None, 
    "y" : None,
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

def f(x, y):
    values = allowed.copy()
    values["x"] = x
    values["y"] = y

    return eval(expression, {"__builtins__": {}}, values)

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
h = float(input("Enter the value of h: "))

result = DerivativeApproximation_in_2D(f, x, y, h)
print(result)