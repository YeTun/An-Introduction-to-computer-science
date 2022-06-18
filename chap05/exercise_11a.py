# Me Computer, Mandalay.
# June 16, 2022
# exercise_11.py
# Chaos function shown on section 1.6 the magic of python improved to contain a better table

# 11. Write an improved version of the chaos.py program from Chapter 1 that allows a user to input two initial values and the number of
#     of iterations, and then prints a nicely formatted table showing how the values change over time. For example, if the starting
#     values were .25 and .26 with 10 iterations, the table might look like this:

#     index    0.25         0.26
#     ----------------------------
#       1    0.731250     0.750360
#       2    0.766441     0.730547
#       3    0.698135     0.767707
#       4    0.821896     0.695499
#       5    0.570894     0.825942
#       6    0.955399     0.560671
#       7    0.166187     0.960644
#       8    0.540418     0.147447
#       9    0.968629     0.490255
#      10    0.118509     0.974630

def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 & 1: "))
    y = float(input("Enter another number between 0 & 1: "))
    n = int(input("Enter the number of iterations to do: "))
    
    print("\n{0} {1:^11} {2:^11}".format("index", x, y))
    print("----------------------------")
    
    for i in range(1, n+1):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{0:>4} {1:^12.6f} {2:^12.6f}".format(i, x, y))

main()


# def main():
#     print("This function demonstraits a chaotic function.")
#     x = float(input("Enter a number between 0 and 1: "))
#     y = float(input("Enter another number between 0 and 1: "))
#     n = int(input("Enter number of values to return: "))
#     table = ["\nindex", x, y, "-"*30]

#     print(f"{table[0]}     {table[1]}         {table[2]}\n{table[3]}")

# # for loop to iterate numbers
#     for i in range(1, n+1):
#         x = 3.9 * x * (1 - x)
#         y = 3.9 * y * (1 - y)
#         print("  {:00.0f}   {:10.6f}   {:10.6f}".format(i, x, y))

# main()

# def main():
#      print("Ths program illustrates a chaotic function")
#      x = float(input("Enter first numbers between 0 and 1: "))
#      y = float(input("Enter second number between 0 and 1: "))
#      z = "input"
     
#      print("{2:<8}{0:<13.2f}{1:<6.2f}".format(x,y,z))
#      print("---------------------------")
     
#      for i in range (10):
#          x = 3.9 * x * (1 - x)
#          y = 3.9 * y * (1 - y)
#          print("{0:>14.6f}{1:>13.6f}".format(x, y))
     
# main()

