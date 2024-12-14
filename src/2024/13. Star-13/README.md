# Idea for claw machines
## Problem
Button A: X+94, Y+34

Button B: X+22, Y+67

Prize: X=8400, Y=5400

So a system of equations that says:
- 94x + 22y = 8400 
- 34x + 67y = 5400 
- 0 <= x <= 100, 0 <= y <= 100 
- Goal(min(x+3y))

or returns 0 if there is no value of x,y that meets these requirements

## Idea for algorithm
Just use scipy
```python
from scipy.optimize import linprog

# Coefficients of the objective function
c = [3,1]

# Equality constraint coefficients
A_eq = [
    [94, 22],
    [34, 67]
]
b_eq = [8400, 5400]

# Bounds for x and y
bounds = [(0, 100), (0, 100)]

# Solve the linear program
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Check the result
if result.success:
    print(f"Optimal value: {result.fun}")
    print(f"Values of x and y: {result.x}")
else:
    print("No solution found")
```