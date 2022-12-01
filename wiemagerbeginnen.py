aantal_spelers = int(input("Hoeveel spelers zijn er... "))
Namen = [] 
#-------------------
import random
for x in range(aantal_spelers):
    Namen_1 = input("Wat zijn de namen van alle spelers die meedoen?")
    print(x)
    Namen.append(Namen_1)
#--------------------
winnaar = random.choice(Namen)
print(winnaar)


