# ME Computer, Mandalay.
# June 24, 2022
# exercise_2.py

class FibCounter:
    def __init__(self):
        self.fibcount = 0

    def getCount(self):
        return self.fibcount

    def fib(self, n):
        self.fibcount += 1
        if n < 3:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
    
    def resetCount(self):
        self.fibcount = 0


count = FibCounter()

count.fib(6)

print(count.getCount())
