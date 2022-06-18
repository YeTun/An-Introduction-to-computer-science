# Me Computer, Mandalay.
# June 19, 2022
# exercise_2.py
# Windchill Table

def main():
    windSpeed = 0
    print("\n       Temp(F):      |-20| |-10| |  0| | 10| | 20| | 30| | 40| | 50| | 60| ")
    print("---------------------------------------------------------------------------")
    while windSpeed <= 50:
        temp = -20
        rowList = ["Windspeed (MPH): {0:3.0f}".format(windSpeed)]
        while temp <= 60:
            windChill = 35.74 + 0.6215*temp - 35.75*(windSpeed ** 0.16) + 0.4275*temp*(windSpeed**0.16)
            rowList.append("|{0:3.0f}|".format(windChill))
            temp += 10
        print(" ".join(rowList))
        windSpeed += 5

main()
