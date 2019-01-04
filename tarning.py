import math
import random

num = 1
i = 0

while num != 6:
    if input("Klicka enter för att slå") == "":
        num = random.randint(1,6)
        print(num)
    i += 1

print("Du fick en sexa efter " + str(i) + " slag")