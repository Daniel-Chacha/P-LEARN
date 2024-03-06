#minimizing a function ; maxima
#We can use scipy.optimize.minimize() function to minimize the function.
#The minimize() function takes the following arguments:
#fun - a function representing an equation.
#x0 - an initial guess for the root.
#method - name of the method to use. Legal values:
# 'CG','BFGS', 'Newton-CG', 'L-BFGS-B','TNC', 'COBYLA','SLSQP'
#callback - function called after each iteration of optimization.
#options - a dictionary defining extra params:
  # "disp": boolean - print detailed description
     #"gtol": number - the tolerance of the error

#minimize the function x^2 +x +2  with BFGS
from scipy.optimize import minimize

def eqn(x):
    return x**2 +x +2

y=minimize(eqn,0,method='BFGS')
print(y.x)
#all info about solution
print(y)