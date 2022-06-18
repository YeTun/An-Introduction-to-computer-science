# Me Computer, Mandalay.
# June 17, 2022
# exercise_1.py
# This programprints the lyrics to "Old McDonald" childrens song

def chorus():
    print("Old McDonald had a farm, Ee-igh, Ee-igh, Oh!")

def farm(animal, noise):
    chorus()
    print("And on that farm he had a", animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a" ,noise + ",", noise, "here and a", noise + ",", noise, "there" )
    print("Here a", noise + ", there a", noise + ", everywhere a", noise, noise)
    chorus()

def main():
    farm("cow", "moo")
    print()
    farm("cat", "meow")
    print()
    farm("dog", "bark")
    print()
    farm("crow", "caw")
    print()
    farm("horse", "neigh")

main()


# def oldMac():
#     print("Old MacDonald had a farm, Ee-igh, Ei-igh, Oh!")

# def animal(animal, sound):
#     oldMac()
#     print("And on this farm he had a(n)", animal +", Ee-igh, Ee-igh, Oh!")
#     print("With a(n)", sound + ",", sound, "here, and a(n)", sound+",", sound, "there.")
#     print("Here a(n)", sound+",","there a(n)", sound + ",", "everywhere a(n)", sound+",", sound+".")
#     oldMac()

# def main():
#     animal('pig', 'oink')

#     print()
#     animal('chicken', 'cheep')

#     print()
#     animal('frog', 'ribbit')

#     print()
#     animal('goat', 'bah')

# main()
