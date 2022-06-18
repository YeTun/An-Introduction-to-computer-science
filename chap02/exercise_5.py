# ME Computer, Mandalay.
# June 13, 2022
# exercise_5.py

#  5. Modfiy the convert.py program (Section 2.2) so that it computes and prints 
#     a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees 
#     from 0 degress celsius to 100 degrees celsius.

#converstionchart.py
#     A program to compute and print a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees
#     from 0 degrees celsius to 100 degrees celsius

def main():
    print("Celisus Temperatures and")
    print("Their Fahrenheit Equivalents")
    print("{0:<10}{1:<10}".format("C", "F"))
    print("---------------")

    for i in range(11):
        celsius = 10 * i

        fahrenheit = int(9/5 * celsius + 32)
        
        print("{0:<10}{1:<10}".format(celsius, fahrenheit))
        
main()