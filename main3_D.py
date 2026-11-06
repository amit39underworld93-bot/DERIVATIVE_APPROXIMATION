import math

def DerivativeApproximation_in_3D(f, x, y, z, h):

    print("\n==== CHOOSE DIFFERENTIATION METHOD ====")
    print("1. Differentiate with respect to x")
    print("2. Differentiate with respect to y")
    print("3. Differentiate with respect to z")

    choice = int(input("Enter your choice between 1 to 3: "))

    if choice == 1:
        return (f(x+h, y, z) - f(x, y, z))/h
    elif choice == 2:
        return (f(x, y+h, z) - f(x, y, z))/h
    elif choice == 3:
        return (f(x, y, z+h) - f(x, y, z))/h
    else:
        print("Please enter a valid choice between 1 to 3: ")


# ===============================================================================================================================================================
# FUNCTION INPUT
# ===============================================================================================================================================================

expression = input("Enter the function f(x,y,z): ")

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

def f(x, y, z):
    values = allowed.copy()
    values["x"] = x
    values["y"] = y
    values["z"] = z

    return eval(expression, {"__builtins__": {}}, values)

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))
h = float(input("Enter the value of h: "))

result = DerivativeApproximation_in_3D(f, x, y, z, h)
print(result)