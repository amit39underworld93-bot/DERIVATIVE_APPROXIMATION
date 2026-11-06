import math

def DerivativeApproximation_in_1D(f, x, h):

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
        print("Please enter a valid choice between 0 to 3: ")


# ===============================================================================================================================================================
# FUNCTION INPUT
# ===============================================================================================================================================================

expression = input("Enter the function f(x): ")

allowed = {
    "x" : None, 
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

def f(x):
    values = allowed.copy()
    values["x"] = x

    return eval(expression, {"__builtins__": {}}, values)

x = float(input("Enter the value of x: "))
h = float(input("Enter the value of h: "))

result = DerivativeApproximation_in_1D(f, x, h)
print(result)