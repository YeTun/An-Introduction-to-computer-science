def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    if fahrenheit > 90:
        print("It's really hot outside.")
    if fahrenheit < 30:
        print("It's really cold outside.")

main()