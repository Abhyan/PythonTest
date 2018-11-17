favAnimal = input("What is your favourite animal? ")

if (favAnimal.upper() == "DOG" or favAnimal.upper() == "DOGS"):
    print("So is mine!")
else:
    print("{0} is good too".format(favAnimal))