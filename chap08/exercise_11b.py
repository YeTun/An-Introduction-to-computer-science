# Me Computer, Mandalay.
# June 19, 2020
# exercise_11.py

# This program accepts a sequence of average daily temps and computes
# the running total of cooling and heating degree days

def main():
    avgTemp = 0
    coolDeg = 0
    heatDeg = 0
    while True:
        # Accept input in degrees
        avgTemp = input("Enter average daily temperature (Type 'Exit' to quit)>> ")
        if avgTemp.lower() == "exit":
            break
        else:
            try:
                avgTemp = int(avgTemp)

                if avgTemp < 60:
                    coolDeg = coolDeg + abs((avgTemp - 60))
                elif avgTemp > 80:
                    heatDeg = heatDeg + (avgTemp - 80)
                else:
                    avgTemp = avgTemp
            except ValueError:    
                print("Make sure your input is a number.")
            except IndexError:
                print("Make sure your input is a number.")                

    print(f"The cooling degree-day is {coolDeg} and the heating degree-day is {heatDeg}")

main()
