# Derivative Approximation Engine 📉

A custom, pure Python Command-Line Interface (CLI) engine designed to compute numerical derivatives dynamically. 
This toolkit calculates the rate of change for single and multivariable functions across 1D, 2D, and 3D vector spaces from scratch, utilizing foundational numerical calculus theorems without external scientific libraries.

## 🚀 Key Features

- **Multi-Dimensional Differentiation:** Dynamically parses and evaluates continuous functions in $1D$ $f(x)$, $2D$ $f(x,y)$, and $3D$ $f(x,y,z)$ forms.

- **Approximation Methods:**

  - **1D Calculus:** Supports user-selected Forward Difference, Backward Difference, and Central Difference methods.
    
  - **Partial Derivatives (2D/3D):** Allows users to selectively differentiate the function with respect to $x$, $y$, or $z$ to compute specific gradient components.

- **Dynamic Parsing with Safety Constraints:** Evaluates user-inputted mathematical strings (e.g., `sin(x) * exp(y)`) dynamically using Python's `eval()` within a strictly bounded dictionary.
This dictionary allows only safe and standard functions from Python's built-in `math` module to prevent arbitrary code execution.

- **Error Handling:** Implements `ZeroDivisionError` catching when the step size ($h$) is explicitly entered as $0$.

## 🛠️ Tech Stack
- **Language:** Python 3

- **Core Logic:** Raw numerical mathematics implementing Finite Difference Methods (Forward, Backward, and Central). Built-in `math` module is used for evaluating trigonometric and logarithmic functions.

## 💻 How to Run (Installation & Execution)

*This project requires zero external dependencies (no NumPy or SciPy required).*

1. ### Clone the repository:

   git clone https://github.com/amit39underworld93-bot/DERIVATIVE_APPROXIMATION.git cd DERIVATIVE_APPROXIMATION

2. ### Execute the desired script:
  *You can run the unified engine or specific dimension scripts.*

  - **For 1D Differentiation:** `python3 main1_D_2.py`

  - **For 2D Differentiation:** `python3 main2_D_2.py`
  
  - **For 3D Differentiation:** `python3 main3_D_2.py`
  
  - **For Unified Multi-Dimensional Engine:** `python3 derivative_approximation.py`

## 📸 Usage Example

*When you run the unified derivative_approximation.py script, follow the interactive terminal prompts:*

***Example: 2D Partial Derivative***

Enter the dimension from 1D to 3D: 2

==== CHOOSE DIFFERENTIATION METHOD ====

1. Differentiate with respect to x
  
2. Differentiate with respect to y
   
Enter your choice between 1 to 2: 1

Enter the function f(x, y): x**2 * y

Enter the value of x: 3

Enter the value of y: 4

Enter the value of h (step size): 0.0001

***The application will output the precise numerical approximation of the partial derivative at the given coordinates.***
