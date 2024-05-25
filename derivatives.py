import sympy as sym

x=sym.Symbol('x')       #symbolize x
func=x**4 +4*x**2 +5*x +6

sym.Derivative(func,x)

sym.Derivative(func,x,evaluate=True)

# func.diff(x)     this does the same

expr=sym.lambdify(x,func)
expr_der=sym.lambdify(x,func.diff(x))


print(f'Value of func at x=5 :'{expr(5)})
print(f'derivative of func at x=5:')