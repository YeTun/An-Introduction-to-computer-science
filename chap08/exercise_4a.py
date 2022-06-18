# Me Computer, Mandalay.
# June 19, 2022
# exercise_4.py
# Syracuse sequence

def syracuseFunction(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def main():
    startValue = int(input("Enter a natural number > 0 (i.e. 1968): "))
    
    print(f"Starting value is: {startValue:0.0f}")
    while startValue != 1:
        startValue = syracuseFunction(startValue)
        print("Current value is: {0:0.0f}".format(startValue))

main()
