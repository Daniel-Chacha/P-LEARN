def fibonacci_iterative(n):
    fib_sequence=[0,1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[-1] +fib_sequence[-2])
    return fib_sequence

sequence=fibonacci_iterative(5)
print(sequence)