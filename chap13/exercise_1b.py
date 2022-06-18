# ME Computer, Mandalay.
# June 24, 2022
# exercise_1.py

count = 0
def recFib(n):
    # returns nth Fibonacci number
    # Note: this algorithm is exceedingly inefficient!
    global count
    
    print(f"Computing fib({n})")
    if n < 3:
        return 1
    else:
        print(f"Leaving fib({n}), returning {recFib(n-1) + recFib(n-2)}")
        if n == 3:
            count += 1
        return recFib(n-1) + recFib(n-2)

result = recFib(10)
print(f"The result is {result} and fib(3) is {count}.")