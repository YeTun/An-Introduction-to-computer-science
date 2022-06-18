def sieveList(n):
    not_prime = []
    prime = []
    for i in range(2, n + 1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i*i, n+1, i):
                not_prime.append(j)
    return prime

def inputs():
    validData = False
    while validData == False:
        try:
            n = eval(input("Please enter a number greater than 2: "))
            if n > 2:
                validData = True
            else:
                print("Your number must be greater than 2")
        except TypeError:
            print("Please enter a number")
    return n

def intro():
    print("This program uses the Sieve of Eratosthenes to determine if a number is prime")

def main():
    intro()
    n = inputs()
    prime = sieveList(n)
    print(prime)

main()